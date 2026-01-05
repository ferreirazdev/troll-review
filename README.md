# 🔥 CODE ROASTER 3000 🔥

> *The AI-powered code reviewer that will absolutely destroy your code... constructively.*

A brutally honest command-line tool that uses Google's Gemini AI to roast your code like a senior engineer who's had one too many code reviews. Get ready for sarcasm, wit, and actual helpful feedback.

**Architectural Fundamentals:** Built with Clean Architecture principles, implementing Dependency Injection and the Port/Adapter pattern to ensure separation of concerns between domain logic, application use cases, and infrastructure implementations. The project follows SOLID principles, particularly Dependency Inversion, allowing easy swapping of LLM providers without modifying core business logic. This architecture ensures maintainability, testability, and extensibility while keeping the domain layer completely independent of external frameworks.

## ✨ Features

- 🔥 **Brutally Honest Reviews**: Get roasted by AI that doesn't hold back
- 💀 **Sarcastic but Helpful**: We'll make fun of your code, but we'll also fix it
- 🎯 **Interactive CLI**: Real-time code roasting with a beautiful (and sassy) interface
- 💾 **Auto-Save Reviews**: All reviews are automatically saved as markdown files for future reference
- 🔐 **Flexible Auth**: Works with API keys or service accounts (we're not picky)
- 🏗️ **Clean Architecture**: Because even trolls need good code structure

## 🚀 Quick Start

### Prerequisites

- Python 3.13+ (because we use modern stuff, not ancient Python 2.7)
- A Google Gemini API key ([Get one here](https://aistudio.google.com/apikey)) OR a service account JSON file

### Installation

1. **Clone this masterpiece:**
```bash
git clone <repository-url>
cd ai_code_reviewer
```

2. **Create a virtual environment** (because you're not a monster):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Option 1: API Key (The Easy Way) 🎯

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Set it up:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

**Or use a `.env` file** (because we support modern practices):
```
GEMINI_API_KEY=your-api-key-here
```

**Make it permanent** (so you don't have to do this every time):
```bash
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### Option 2: Service Account (The Enterprise Way) 🏢

If you have a Google Cloud service account JSON file:

1. Drop it in the project root (e.g., `credentials.json`)
2. **Enable Vertex AI API** (because Google requires it):
   - Visit: https://console.developers.google.com/apis/api/aiplatform.googleapis.com/overview?project=YOUR_PROJECT_ID
   - Click "Enable" (it's not that hard)
   - Wait a few minutes (patience is a virtue)
3. The tool will automatically find and use it (we're smart like that)

**Or point to it directly:**
```bash
export GEMINI_API_KEY="/path/to/your/service-account.json"
```

## 🎮 Usage

### Interactive Mode (The Fun Way) 🎪

Run without arguments and enter the roasting zone:

```bash
python cmd/cli.py
```

**What you'll see:**
```
======================================================================
🔥                    CODE ROASTER 3000                    🔥
======================================================================
🤖 The AI that will be brutally honest about your code
💀 Prepare to be roasted (but also helped)
======================================================================

🔍 Checking if you're actually configured...
✅ ✓ Configuration valid: Using GEMINI_API_KEY from AI Studio

✨ Ready to absolutely destroy your code (constructively)!

📋 Commands:
  - Enter a file path to get roasted 🔥
  - Type 'exit' or 'quit' to escape
  - Type 'help' if you're lost
----------------------------------------------------------------------

😈 Enter your code path (or 'exit' to quit): src/main.py
🔥 Preparing to roast: src/main.py
⏳ Analyzing your code like a trainee wrote it...

======================================================================
🔥                         THE ROAST                         🔥
======================================================================
[Your code gets absolutely destroyed here... but constructively]
======================================================================

💾 Review saved to: reviews/main_review_20250101_143022.md

💀 Hope you learned something! (You probably did)
```

### Non-Interactive Mode (The Quick Way) ⚡

Review a single file and get roasted immediately:

```bash
python cmd/cli.py path/to/your/file.py
```

**Examples:**

```bash
# Python file
python cmd/cli.py src/main.py

# JavaScript file
python cmd/cli.py app/index.js

# Any code file (we're not picky)
python cmd/cli.py examples/example.go
```

## 🎯 What You'll Get

The AI will roast your code with:

- **Sarcastic Summary**: "You code like a trainee who just discovered copy-paste"
- **Brutal Issues**: "This looks like it was written at 3 AM after 5 energy drinks"
- **Actual Suggestions**: Real fixes that will make your code less... terrible

### 💾 Review Files

Every review is automatically saved to a markdown file in the `reviews/` directory with:
- Original file path
- Review timestamp
- Full review content
- Formatted for easy reading

**File naming:** `filename_review_YYYYMMDD_HHMMSS.md`

Example: `main_review_20250101_143022.md`

Perfect for:
- Keeping track of code improvements over time
- Sharing reviews with your team
- Building a portfolio of your code evolution
- Proving to your boss that you're actually improving

## 🏗️ Project Structure

```
ai_code_reviewer/
├── application/
│   └── usecases/
│       └── review_code.py      # The roasting logic
├── cmd/
│   └── cli.py                  # The beautiful (and sassy) CLI
├── container.py                # Dependency injection (fancy stuff)
├── domain/
│   └── ports.py                # Interfaces (because we're professional)
├── infrastructure/
│   └── llm/
│       └── gemini_client.py    # Talks to Google's AI
├── reviews/                    # Auto-generated review markdown files
│   └── *.md                    # Your roasted code reviews
├── requirements.txt            # Dependencies (obviously)
└── README.md                   # This file (you're reading it)
```

## 🛠️ Tech Stack

- **Python 3.13+**: Because we like modern Python
- **Google Gemini AI**: The AI that roasts your code
- **Clean Architecture**: Because even trolls need structure
- **python-dotenv**: For `.env` file support (we're not savages)

## 🐛 Troubleshooting

### "API key not valid" 💥
- Make sure you're using an actual API key string, not a file path
- Check if your API key is still valid (they expire sometimes)
- Get a fresh one from [Google AI Studio](https://aistudio.google.com/apikey)

### "Vertex AI API has not been used" 🏢
- You're using a service account but forgot to enable Vertex AI
- Go to Google Cloud Console and enable it (it's literally one click)
- Wait a few minutes (Google needs time to process your request)

### "GEMINI_API_KEY not found" 🔍
- Set it: `export GEMINI_API_KEY="your-key"`
- Or drop a service account JSON file in the project root
- Or create a `.env` file (we support that too)

## 🤝 Contributing

Found a bug? Want to make it even more sarcastic? PRs welcome!

1. Fork it
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Google Gemini AI for powering the roasts
- All the developers whose code got roasted (you made this possible)
- The Python community for making this possible

---

**Made with 💀 and 🔥 by someone who's seen too much bad code**

*Remember: We roast because we care. Your code will thank you later.*
