import os
import subprocess

def run_python_file(working_dir, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_dir)
    abs_access_file = os.path.abspath(os.path.join(working_dir, file_path))
    
    if not os.path.commonprefix([abs_working_dir, abs_access_file]) == abs_working_dir:
        return f'Error: Cannot list "{abs_access_file}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_access_file):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    stdout = ""
    stderr = ""

    try:
        process = subprocess.run(["python3", abs_access_file, *args], capture_output=True, timeout=30)

        process_status = ""
        if len(process.stdout) != 0:
            process_status = f"STDOUT: {process.stdout}, "

        if len(process.stderr) != 0:
            process_status = f"STDERR: {process.stderr}, "

        if process.returncode != 0:
            return f"Process exited with code {process.returncode}"

        if len(process_status) == 0:
            return "No output produced."

        return process_status
    

    except Exception as e:
        return f"Error: executing Python file: {e}"
