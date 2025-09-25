import os


def write_file(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    abs_access_file = os.path.abspath(os.path.join(working_dir, file_path))


    if not os.path.commonprefix([abs_working_dir, abs_access_file]) == abs_working_dir:
        return f'Error: Cannot list "{abs_access_file}" as it is outside the permitted working directory'
    
    try:
        with open(abs_access_file, "w") as f:
            f.write(content) 
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as error:
        os.crea
    
    if not os.path.isfile(abs_access_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'