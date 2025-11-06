import os

def write_file(working_directory, file_path, content):
    working_abs = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(file_path)
    full_path = os.path.join(working_abs, file_path)
    file_parent_dir = os.path.dirname(full_path)

    if not (full_path == working_abs or full_path.startswith(working_abs + os.path.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        if not os.path.exists(abs_file_path):
            if not os.path.exists(file_parent_dir):
                os.makedirs(file_parent_dir)
    except:
        return f'Error: File path could not be created'
    
    try:
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f'Error: failed to write content to file'
