from google.genai import types

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