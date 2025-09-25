import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt


def main():
    res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[define_functions_schema()]))

    if (isinstance(res.text, str)):
        print(res.text)

    if res.function_calls != None and len(res.function_calls) > 0:
        for call_fn in res.function_calls:
            print(f"Calling function: {call_fn.name}({call_fn.args})")

    if g_flags["verbose"]:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

def parse_arguments():
    try:
        prompt = sys.argv[1]
    except:
        prompt = None

    if not isinstance(prompt, str):
        print("Argument for prompt not provided or is invalid")
        exit(1)

    messages.append(
        types.Content(role="user", parts=[types.Part(text=prompt)])
    )

    arg_flags = sys.argv[2:]
    for flag in arg_flags:
        if not flag.startswith("--"):
            continue

        flag_name = flag.removeprefix("--")
        if flag_name in g_flags:
            g_flags[flag_name] = True

def define_functions_schema():
    schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    return types.Tool(
        function_declarations=[
            schema_get_files_info
        ]
    )
        

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = []
    g_flags = {
        "verbose": False 
    }

    parse_arguments()
    main()
