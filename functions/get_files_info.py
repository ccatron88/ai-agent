import os

def get_files_info(working_directory, directory="."):
    working_abs = os.path.abspath(working_directory)
    file_path = os.path.join(working_abs, directory)
    absolute_path = os.path.abspath(file_path)
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
