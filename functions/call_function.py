from functions import get_files_info as gfi
from functions import get_file_content as gfc
from functions import write_file as wc
from functions import run_python_file as rpf
from google.genai import types


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    availabe_functions = {
        "get_files_info": gfi.get_files_info,
        "get_file_content": gfc.get_file_contents,
        "write_file": wc.write_file,
        "run_python_file": rpf.run_python_file,
    }

    if not function_call_part.name in availabe_functions:
        return  types.Content(
                    role="tool",
                    parts=[
                        types.Part.from_function_response(
                            name=function_call_part.name,
                            response={"error": f"Unknown function: {function_call_part.name}"},
                        )
                    ],
                )

    fn_result =  availabe_functions[function_call_part.name]("./calculator", **function_call_part.args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": fn_result},
            )
        ],
    )
