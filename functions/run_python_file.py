import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a given executable in python format. Receives optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Full filepath to an executable to be run.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional arguments to pass to an executable"
            )
        },
    ),
)

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

    
