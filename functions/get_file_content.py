import os
from config import MAX_CHAR_NUM_IN_FILE

def get_file_contents(working_dir, file_path):
    abs_working_dir = os.path.abspath(working_dir)
    abs_access_file = os.path.abspath(os.path.join(working_dir, file_path))
    
    if not os.path.commonprefix([abs_working_dir, abs_access_file]) == abs_working_dir:
        return f'Error: Cannot list "{abs_access_file}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_access_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'


    try:
        with open(abs_access_file, "r") as f:
            file_content_string = f.read(MAX_CHAR_NUM_IN_FILE + 1)

            if len(file_content_string) > MAX_CHAR_NUM_IN_FILE:
                file_content_string = file_content_string[:-1] + f'[...File "{file_path}" truncated at {MAX_CHAR_NUM_IN_FILE} characters]'

            return file_content_string

    except Exception as error:
        return f'Error: {str(error)}'