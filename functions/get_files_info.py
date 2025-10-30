import os

def get_files_info(working_directory, directory="."):
    working_abs = os.path.abspath(working_directory)
    file_path = os.path.join(working_abs, directory)
    absolute_path = os.path.abspath(file_path)
    
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
