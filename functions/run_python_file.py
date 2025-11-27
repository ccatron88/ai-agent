import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    working_abs = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_abs, file_path))
    
    if os.path.commonpath([working_abs, full_path]) != working_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if not full_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    cmd = ['python', file_path] + list(args)

    try:
        result = subprocess.run(cmd, cwd=working_abs, timeout=30, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        return_string = f'STDOUT: {stdout}STDERR: {stderr}'.rstrip()

        if not result.stderr and not result.stdout:
           return 'No output produced.'
        if result.returncode != 0:
            return f'{return_string}\nProcess exited with code {result.returncode}'
        

        return return_string
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

    
