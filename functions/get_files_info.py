import os

def get_files_info(working_directory, directory="."):
    file_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(file_path)
    is_dir = os.path.isdir(file_path)
    size = os.path.getsize(file_path)

    print(working_directory)
    print(directory)
    print(file_path)
    print(absolute_path)

    
    if not absolute_path.startswith(file_path[:-2]):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')    
    
    if not is_dir:
        return (f'Error: "{directory}" is not a directory')
    
    return (f"{directory} file_size={size} is_dir={is_dir}")

print (get_files_info((os.getcwd())))
