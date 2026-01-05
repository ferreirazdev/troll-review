# AI Code Reviewer

A command-line tool that uses Google's Gemini AI to review code and provide feedback, including summaries, issues, and suggestions.

## Features

- Automated code review using Gemini AI
- Provides code summaries, identifies issues, and suggests improvements
- Interactive CLI mode for real-time code reviews
- Support for both API key and service account authentication
- Clean architecture with separation of concerns

## Prerequisites

- Python 3.13 or higher
- One of the following:
  - A Google Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey) (recommended)
  - A Google Cloud service account JSON file with Vertex AI API enabled

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai_code_reviewer
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The tool supports two authentication methods:

### Option 1: API Key (Recommended - Simplest)

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Using environment variable:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Using .env file:**
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your-api-key-here
```

**Make it permanent:**
Add it to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### Option 2: Service Account JSON File

If you have a Google Cloud service account JSON file:

1. Place the JSON file in the project root (e.g., `igoove-95cf35b968d2.json`)

2. **Important:** Enable Vertex AI API in your Google Cloud project:
   - Visit: https://console.developers.google.com/apis/api/aiplatform.googleapis.com/overview?project=YOUR_PROJECT_ID
   - Click "Enable"
   - Wait a few minutes for it to propagate

3. The tool will automatically detect and use the JSON file

**Alternative:** Set `GEMINI_API_KEY` to the JSON file path:
```bash
export GEMINI_API_KEY="/path/to/your/service-account.json"
```

## Usage

### Interactive Mode (Recommended)

Run the CLI without arguments to enter interactive mode:

```bash
python cmd/cli.py
```

This will:
1. Validate your configuration
2. Enter an interactive loop where you can:
   - Enter file paths to review
   - Type `help` for commands
   - Type `exit` or `quit` to exit

**Example session:**
```
============================================================
🤖 AI Code Reviewer - Interactive Mode
============================================================

🔍 Validating configuration...
✓ Configuration valid: Using GEMINI_API_KEY from AI Studio

✓ Ready to review code!

Commands:
  - Enter a file path to review it
  - Type 'exit' or 'quit' to exit
  - Type 'help' for help
------------------------------------------------------------

📁 File path (or 'exit' to quit): src/main.py
📝 Reviewing: src/main.py
⏳ Generating review...

============================================================
📊 REVIEW RESULTS
============================================================
[Review output here...]
============================================================
```

### Non-Interactive Mode

Review a single file by providing the file path as an argument:

```bash
python cmd/cli.py path/to/your/file.py
```

**Examples:**

Review a Python file:
```bash
python cmd/cli.py src/main.py
```

Review a JavaScript file:
```bash
python cmd/cli.py app/index.js
```

Review any code file:
```bash
python cmd/cli.py examples/example.go
```

## How It Works

1. The tool reads the code from the specified file
2. Sends it to Gemini AI for review
3. Displays the review results, including:
   - Summary
   - Issues found
   - Suggestions for improvement

## Project Structure

```
ai_code_reviewer/
├── application/
│   └── usecases/
│       └── review_code.py      # Use case for code review
├── cmd/
│   └── cli.py                  # Command-line interface
├── container.py                # Dependency injection container
├── domain/
│   └── ports.py                # Domain interfaces
├── infrastructure/
│   └── llm/
│       └── gemini_client.py    # Gemini AI client implementation
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Troubleshooting

### "API key not valid" error
- Make sure your `GEMINI_API_KEY` is set to an actual API key string, not a file path
- Verify the API key is correct and active
- Get a new API key from [Google AI Studio](https://aistudio.google.com/apikey)

### "Vertex AI API has not been used" error
- If using a service account JSON file, you need to enable Vertex AI API
- Visit your Google Cloud Console and enable the API for your project
- Wait a few minutes after enabling for it to propagate

### "GEMINI_API_KEY not found" error
- Set the environment variable: `export GEMINI_API_KEY="your-key"`
- Or place a service account JSON file in the project root
- Or create a `.env` file with `GEMINI_API_KEY=your-key`

## License

[Add your license here]
