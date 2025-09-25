import os
import sys
from dotenv import load_dotenv
from google import genai


def main():
    res = client.models.generate_content(model="gemini-2.0-flash-001", contents=get_prompt())
    print(res.text)
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

def get_prompt():
    try:
        prompt = sys.argv[1]
    except:
        prompt = None

    if not isinstance(prompt, str):
        print("Argument for prompt not provided or is invalid")
        exit(1)

    return prompt
        

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    main()
