import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_abs = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(file_path)
    full_path = os.path.join(working_abs, file_path)

    print(full_path.startswith(working_abs))

    if not (full_path == working_abs or full_path.startswith(working_abs)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    result = subprocess.run(abs_file_path, timeout=30, capture_output=True, args=args)

    # print(result)
    return result
