import os
from google.genai import types


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
    description="Read file content, constrained to a max character limit.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "read": types.Schema(
                type=types.Type.STRING,
                description="Read content of selected files.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a given executable in python format. Receives optional arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "execute": types.Schema(
                type=types.Type.STRING,
                description="Execute a python file with given arguments.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a given file with received content data.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "write": types.Schema(
                type=types.Type.STRING,
                description="Write or overwrite a given file with content provided to function.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    working_abs = os.path.abspath(working_directory)
    file_path = os.path.join(working_abs, directory)
    absolute_path = os.path.abspath(file_path)

    print(absolute_path == working_abs)
    print(absolute_path.startswith(working_abs + os.sep))
    print(absolute_path)
    print(working_abs + os.sep)
    
    if not (absolute_path == working_abs or absolute_path.startswith(working_abs + os.sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        names = os.listdir(absolute_path)
    except Exception as e:
        return f"Error: {e}"
    
    lines = []
    for name in names:
        entry_path = os.path.join(absolute_path, name)
        is_dir = os.path.isdir(entry_path)

        try:
            size = os.path.getsize(entry_path)
            line = f"- {name}: file_size={size} bytes, is_dir={is_dir}"
        except Exception as e:
            line = f"- {name}: file_size=Error({e}), is_dir={is_dir}"
        lines.append(line)
        
    return "\n".join(lines)
