# Content Creator AI Tool

A simple, robust Python tool for content creators to **summarize** and **rephrase** text using **OpenAI's GPT-3.5/4**.

## Features

- **Summarization**: Condenses long articles or paragraphs into 2-3 concise sentences.
- **Rephrasing**: Rewrites text in an engaging and professional tone.
- **Custom Tones**: You can specify any tone (e.g., "Shakespearean", "Pirate").
- **Text Limits**: Enforces a safe input limit (default 64,000 chars) to prevent errors.

See [Prompt Engineering & Error Handling](prompt_engineering.md) for design details.

## Setup

1. **Prerequisites**:
   - Python 3.8+
   - An OpenAI API Key (Get one from [OpenAI Platform](https://platform.openai.com/))

2. **Installation**:
   ```bash
   # Navigate to the project folder
   cd /path/to/Summarizer

   # Create a virtual environment (optional but recommended)
   python3 -m venv venv
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Set your API key as an environment variable:
   ```bash
   export OPENAI_API_KEY="your-sk-key-here"
   ```

## Usage

### Method 1: Interactive Mode
Run the script without arguments to paste text directly:
```bash
python content_tool.py
```
*Select option 1, then paste your text and press Enter twice.*

### Method 2: File Mode
Provide a text file as an argument:
```bash
python content_tool.py input.txt
```

## Limits & Warnings

- **Max Input**: ~64,000 characters (approx. 16k tokens) to avoid token limit errors.
- **Cost**: This tool uses OpenAI API, which is a paid service (though very cheap for text). Ensure your account has credits.
