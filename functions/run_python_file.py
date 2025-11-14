import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_abs = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(file_path)
    full_path = working_abs + abs_file_path

    if not working_abs == abs_file_path or working_abs.startswith(abs_file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    subprocess.run(run_python_file, timeout=30, stdout=True, stderr=True, args=args)
