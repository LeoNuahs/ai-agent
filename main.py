import os
import sys

from dotenv import load_dotenv
from google import genai

def main():
    # CLI arguments
    args = sys.argv[1:]

    if len(args) == 0:
        print("Please provide a prompt")
        os._exit(1)

    _ = load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=args
    )

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
