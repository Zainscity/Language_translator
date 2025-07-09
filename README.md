# 🌐 Multi-Language Translator using AI Agents

This is a powerful command-line based multilingual translator that uses Google's **Gemini API** with custom-built **AI agents** to translate text from English, Roman Urdu, and Hindi into over 50 world languages.

It uses an agent-based architecture to intelligently route the user's translation request to the appropriate language agent.

---

## ✨ Features

- 🔁 Supports translation from **English**, **Roman Urdu**, and **Hindi**
- 🌍 Translates into 50+ languages including Spanish, French, German, Urdu, Chinese, Arabic, Russian, Japanese, and many more
- 🧠 AI agents powered by **Gemini 2.0 Flash** model
- 🚀 Built with the [Panaverse Agentic AI framework](https://github.com/panaversity/learn-agentic-ai)
- ⚡ Asynchronous execution with `asyncio`
- 🔒 Secure API usage with `.env` file

---

## 📂 Folder Structure

hello_agent/
├── main.py
├── .env
├── agents/
│ ├── agent.py
│ └── ...
├── pyproject.toml

yaml
Copy
Edit

---

## 🔧 Requirements

- Python 3.11+
- `uv` (for dependency management)
- A **free Gemini API Key** from [Google AI Studio](https://makersuite.google.com/app/apikey)

---

## 📥 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/hello_agent.git
cd hello_agent

# Set up virtual environment and install dependencies
uv venv
uv pip install -r requirements.txt  # or just use `uv add python-dotenv` if needed
🔐 Environment Setup
Create a .env file with your Gemini API Key:

ini
Copy
Edit
GEMINI_API_KEY=your-gemini-api-key-here
🚀 Run the Translator
bash
Copy
Edit
uv run main.py
Then follow the on-screen prompts:

vbnet
Copy
Edit
Welcome to the Multi-Language Translator!
Enter the English text to translate: Hello, how are you?
Available Languages:
Spanish
French
...
Enter the language to translate into: urdu
🌐 Supported Languages
More than 50+ target languages including:

✅ Regional: Urdu, Hindi, Sindhi, Punjabi, Pashto, Bengali, Tamil, Telugu

✅ International: Spanish, French, Arabic, Chinese, Russian, Japanese, German

✅ Less Common: Zulu, Lao, Amharic, Somali, Kurdish, Kazakh, Slovak, and more
