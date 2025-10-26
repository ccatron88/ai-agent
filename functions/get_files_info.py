import os

def get_files_info(working_directory, directory="."):
    file_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(file_path)
    is_dir = os.path.isdir(absolute_path)
    size = os.path.getsize(file_path)
    
    try:
        absolute_path.startswith(file_path[:-2])
    except:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    try:
        os.path.isdir(absolute_path)
    except:
        return f'Error: "{directory}" is not a directory'
    
    return f"{os.listdir(file_path)}: file_size={size} bytes, is_dir={is_dir}"
