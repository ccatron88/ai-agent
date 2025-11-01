import os

def write_file(working_directory, file_path, file):
    working_abs = os.path.abs(working_directory)
    full_path = os.path.join(working_abs, file_path)

    if not full_path == working_abs or full_path.startswith(file_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    
