import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt
from functions import call_function as cf


def main():
    res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[define_functions_schema()]))

    if (isinstance(res.text, str)):
        print(res.text)

    if res.function_calls != None and len(res.function_calls) > 0:
        for call_fn in res.function_calls:
            function_call_result = cf.call_function(call_fn, g_flags["verbose"])

            if not function_call_result.parts[0].function_response.response:
                raise Exception("Unexcpected function response")
            elif g_flags["verbose"]:
                print(f"-> \n{function_call_result.parts[0].function_response.response["result"]}\n=====")
            # print(f"Calling function: {call_fn.name}({call_fn.args})")

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

    schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns contents of the file on the the specified path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to show contents of, relative to the working directory. Function errors if not provided.",
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites the file on specified path with given content or creates a new file with given content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write to, relative to the working directory. New file will be created if file on this path did not exist before.",
                ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content that will be written to the file",
                ),
            },
        ),
    )

    schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes file on given path with passed arguments. Only works for files with .py extension. Function will return if executed file returned a value on STDOUT or error on STDERR.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to be executed, relative to the working directory. Has to be a python file.",
                ),
            "args": types.Schema(
                type=types.Type.OBJECT,
                description="List of arguments to be passed to the function. List is empty by default",
                ),
            },
        ),
    )

    return types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file
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
