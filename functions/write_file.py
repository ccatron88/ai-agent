import os

def write_file(working_directory, file_path, content):
    working_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_abs, file_path)
    print(full_path)

    if not (full_path == working_abs or full_path.startswith(working_abs + os.path.sep)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    else:
        return f'Error: File path could not be created'
    
    try:
        with open(file_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f'Error: failed to write content to file'
