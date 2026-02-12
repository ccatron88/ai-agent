from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from functions.call_function import call_function

# print(run_python_file("calculator", "main.py"))
print(call_function("calculator", "verbose", "main.py"))
print(call_function("calculator", "main.py", ["3 + 5"]))
print(call_function("calculator", "tests.py"))
print(call_function("calculator", "../main.py"))
print(call_function("calculator", "nonexistent.py"))
print(call_function("calculator", "lorem.txt"))
