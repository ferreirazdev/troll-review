import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from container import build_review_code_use_case  # noqa: E402


def validate_config():
    """Validate configuration and return status message."""
    import os

    # Check for API key from Google AI Studio
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        json_path = Path(api_key)
        if json_path.suffix == ".json" and json_path.exists():
            return (
                True,
                f"✓ Configuration valid: Using service account "
                f"({json_path.name})",
            )
        else:
            return (
                True,
                "✓ Configuration valid: Using GEMINI_API_KEY from AI Studio",
            )

    # Check for service account JSON file in project root
    project_root = Path(__file__).parent.parent
    json_files = list(project_root.glob("*.json"))
    for json_file in json_files:
        if (
            json_file.name.startswith("package")
            or json_file.name.startswith("tsconfig")
        ):
            continue
        try:
            # Try to build use case to validate
            _ = build_review_code_use_case()
            return (
                True,
                f"✓ Configuration valid: Using service account "
                f"({json_file.name})",
            )
        except Exception:
            continue

    return (
        False,
        "✗ Configuration invalid: No GEMINI_API_KEY or service account "
        "JSON file found. Get API key from: "
        "https://aistudio.google.com/apikey",
    )


def review_file(use_case, file_path: str):
    """Review a single file and return the result."""
    path = Path(file_path)

    if not path.exists():
        return None, f"✗ Error: File not found: {file_path}"

    if not path.is_file():
        return None, f"✗ Error: Not a file: {file_path}"

    try:
        with open(path, "r", encoding="utf-8") as f:
            code = f.read()

        print(f"\n📝 Reviewing: {file_path}")
        print("⏳ Generating review...\n")

        result = use_case.execute(code)
        return result, None
    except Exception as e:
        return None, f"✗ Error reviewing file: {str(e)}"


def main():
    """Interactive CLI for code review."""
    # Welcome message
    print("=" * 60)
    print("🤖 AI Code Reviewer - Interactive Mode")
    print("=" * 60)
    print()

    # Validate configuration
    print("🔍 Validating configuration...")
    is_valid, message = validate_config()
    print(message)
    print()

    if not is_valid:
        print("Please set GEMINI_API_KEY or add a service account JSON file.")
        sys.exit(1)

    # Build use case
    try:
        use_case = build_review_code_use_case()
    except Exception as e:
        print(f"✗ Failed to initialize: {str(e)}")
        sys.exit(1)

    print("✓ Ready to review code!")
    print()
    print("Commands:")
    print("  - Enter a file path to review it")
    print("  - Type 'exit' or 'quit' to exit")
    print("  - Type 'help' for help")
    print("-" * 60)
    print()

    # Interactive loop
    while True:
        try:
            file_path = input("📁 File path (or 'exit' to quit): ").strip()

            if not file_path:
                continue

            if file_path.lower() in ["exit", "quit", "q"]:
                print("\n👋 Goodbye!")
                break

            if file_path.lower() == "help":
                print("\nCommands:")
                print("  - Enter a file path (relative or absolute)")
                print("  - 'exit' or 'quit' - Exit the program")
                print("  - 'help' - Show this help message")
                print()
                continue

            result, error = review_file(use_case, file_path)

            if error:
                print(error)
                print()
            else:
                print("=" * 60)
                print("📊 REVIEW RESULTS")
                print("=" * 60)
                print(result)
                print("=" * 60)
                print()

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except EOFError:
            print("\n\n👋 Goodbye!")
            break


if __name__ == "__main__":
    # Support both interactive and non-interactive modes
    if len(sys.argv) > 1:
        # Non-interactive mode: single file review
        path = sys.argv[1]
        use_case = build_review_code_use_case()

        result, error = review_file(use_case, path)
        if error:
            print(error, file=sys.stderr)
            sys.exit(1)
        else:
            print(result)
    else:
        # Interactive mode
        main()
