import os
from google import genai
from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

functions_dict = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

def call_function(function_call_part, verbose=False):
    function_call_part.args["working_directory"] = "./calculator"
    function_call_result = functions_dict[function_call_part.name](**function_call_part.args)

    if function_call_part.name not in functions_dict:
        return types.Content(
            role="tool",
            parts=[types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Unknown function: {function_call_part.name}"}
            )]
        )

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    print(f" - Calling function: {function_call_part.name}")

    try:
        function_call_result = functions_dict[function_call_part.name](**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_call_result}
            )]
        )
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[types.Part.from_function_response(
                name=function_call_part.name,
                response={"error": f"Error: {e}"}
            )]
        )
