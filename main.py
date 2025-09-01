import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    _ = load_dotenv()
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]), 
    ]

    generate_content(client, messages, verbose, system_prompt)

def generate_content(client, messages, verbose, system_prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages, 
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt, 
        ),
    )

    if not response.function_calls:
        return response.text

    output = []
    for call in response.function_calls:
        output.append(call_function(call, verbose))

    for call_output in output:
        if not call_output.parts[0].function_response.response:
            print("No response found! Exiting...")
            raise Exception("No response found! Exiting...")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        for call_output in output:
            print(f"-> {call_output.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
