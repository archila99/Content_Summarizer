import os
import sys
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API Key
# Now securely processing from .env file or environment variable
API_KEY = os.getenv("OPENAI_API_KEY")

CLIENT = None

# Using gpt-3.5-turbo as a cost-effective default, or gpt-4 if preferred.
MODEL_NAME = "gpt-3.5-turbo"

# Maximum characters allowed for input text (approx 16k tokens)
MAX_CHAR_LIMIT = 64000

def get_input_text():
    """
    Prompts the user to choose between direct input or reading from a file.
    """
    print("\n--- Content Creator AI Tool (OpenAI Mode) ---")
    print("1. Enter text directly")
    print("2. Read from a text file")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        print("\nEnter your text (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        return "\n".join(lines)
    
    elif choice == '2':
        file_path = input("Enter the path to the text file (e.g., input.txt): ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

def call_openai_api(prompt):
    """
    Calls the OpenAI API.
    """
    global CLIENT
    if not CLIENT:
        CLIENT = OpenAI(api_key=API_KEY)

    try:
        response = CLIENT.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=500  # Adjust as needed
        )
        return response.choices[0].message.content.strip()
            
    except OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return None

def estimate_tokens(text):
    """
    Rough local estimation of tokens (1 token ~= 4 chars).
    """
    return len(text) // 4

def main():
    if not API_KEY:
        print("Error: OPENAI_API_KEY is not set.")
        print("Please export OPENAI_API_KEY='your-key-here'")
        return

    # Check for arguments or use interactive mode
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
             with open(file_path, 'r', encoding='utf-8') as f:
                input_text = f.read()
        except Exception as e:
             print(f"Error reading provided file arg: {e}")
             return
    else:
        input_text = get_input_text()

    if not input_text or not input_text.strip():
        print("No input text provided. Exiting.")
        return

    # Pre-execution warning
    est_tokens = estimate_tokens(input_text)
    print(f"\n--- Input Analysis ---")
    print(f"Length: {len(input_text)} chars")
    print(f"Est. Tokens: ~{est_tokens}")
    
    if len(input_text) > MAX_CHAR_LIMIT:
        print(f"\n(!) Error: Input exceeds the maximum limit of {MAX_CHAR_LIMIT} characters.")
        print("Please reduce the text size and try again.")
        return
    print("----------------------")

    # Ask for custom tone
    tone_input = input("\nEnter a tone for rephrasing (default: 'engaging and professional'): ").strip()
    target_tone = tone_input if tone_input else "engaging and professional"

    print(f"\nProcessing with OpenAI ({MODEL_NAME})...")
    
    # 1. Summarize
    summary_prompt = f"Summarize the following text into 2-3 concise sentences:\n\n{input_text}"
    summary = call_openai_api(summary_prompt)

    # 2. Rephrase
    if summary:
        rephrase_prompt = f"Rephrase the following text in a {target_tone} tone:\n\n{input_text}"
        rephrase = call_openai_api(rephrase_prompt)
        
        if rephrase:
            print("\n" + "="*40)
            print("ORIGINAL TEXT")
            print("="*40)
            print(input_text)
            print("\n" + "="*40)
            print("SUMMARY (2-3 Sentences)")
            print("="*40)
            print(summary)
            print("\n" + "="*40)
            print(f"REPHRASED ({target_tone.capitalize()})")
            print("="*40)
            print(rephrase)
            print("\n" + "="*40)

if __name__ == "__main__":
    main()
