import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, USE_MODEL, MAX_AGENT_ITERATIONS, PROMPT_END_MSG
from functions_schema import define_functions_schema
from functions import call_function as cf

def main():
    for i in range(0, MAX_AGENT_ITERATIONS):
        try:
            generated_content = client.models.generate_content(model=USE_MODEL, contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[define_functions_schema(), ]))
        except Exception as e:
            print(f"Unexpected model exception: {str(e)}")
            break

        if (isinstance(generated_content.text, str)):
            print(generated_content.text)
            if PROMPT_END_MSG in generated_content.text:
                break

        for response_candiate in generated_content.candidates:
            messages.append(response_candiate.content)

        if generated_content.function_calls != None:
            for call_fn in generated_content.function_calls:
                function_call_result = cf.call_function(call_fn, g_flags["verbose"])

                if not function_call_result.parts[0].function_response.response:
                    raise Exception("Unexcpected function response")
                elif g_flags["verbose"]:
                    print(f"-> \n{function_call_result.parts[0].function_response.response["result"]}\n=====")
                
                messages.append(types.Content(role="user", parts=[types.Part(text=function_call_result.parts[0].function_response.response["result"])]))

    if g_flags["verbose"]:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(f"Prompt tokens: {generated_content.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {generated_content.usage_metadata.candidates_token_count}")

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
        

if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = []
    g_flags = {
        "verbose": False,
    }

    parse_arguments()
    main()
