import os

def get_files_info(working_directory, directory="."):
    file_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(file_path)
    readme_is_dir = os.path.isdir((directory + '/README.md'))


    if not file_path.startswith('/Users'):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    
    if not is_dir:
        return (f'Error: "{directory}" is not a directory')
    
    return (f"{} file_size={} is_dir={}")

print (get_files_info((os.getcwd())))
