import os
from google.genai import types
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_file,
        schema_run_python_file,
        schema_get_file_content
    ]
)

def call_function(function_call, verbose=False):
    function_call.args["working_directory"] = "./calculator"
    function_call_result = functions_dict[function_call.name](**function_call.args)
    print(function_call_result)

    function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if function_call.name not in available_functions:
        return types.Content(
            role="tool",
            parts=[types.Part.from_function_response(
                name=function_call.name,
                response={"error": f"Unknown function: {function_call.name}"}
            )]
        )
    function_name = function_call.name or ""

    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    try:
        function_call_result = functions_dict[function_call.name](**function_call.args)
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
