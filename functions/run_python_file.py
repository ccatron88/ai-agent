import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_abs, file_path)

    if not full_path.startswith(working_abs):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    cmd = ['python', file_path] + args

    try:
        result = subprocess.run(cmd, cwd=working_abs, timeout=30, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return_string = f'STDOUT: {result.stdout}STDERR: {result.stderr}'.rstrip()

        
        if result.returncode != 0:
            return f'{return_string}\nProcess exited with code {result.returncode}'
        if not result.stderr and not result.stdout:
           return 'No output produced.'

        return return_string
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

    
