import os
from functions.config import MAX_CHARS


def get_file_content(working_directory, file_path):
    working_abs = os.path.abspath(working_directory)
    full_path = os.path.join(working_abs, file_path)

    if not (full_path == working_abs or full_path.startswith(working_abs)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)

    return file_content_string
