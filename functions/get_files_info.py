import os

def get_files_info(working_directory, directory="."):
    file_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(file_path)

    print(working_directory)
    print(directory)
    print(file_path)
    print(absolute_path)


    if not absolute_path.startswith(file_path[:-2]):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    else:
        print(f"{file_path[:-2]} {absolute_path}")
    
    return os.getcwd()
    
    # if not is_dir:
    #     return (f'Error: "{directory}" is not a directory')
    
    # return (f"{} file_size={} is_dir={}")

print (get_files_info((os.getcwd())))
