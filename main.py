import os
import sys
from dotenv import load_dotenv
from functions.call_function import call_function, available_functions
from google import genai
from google.genai import types

def main():
    load_dotenv()

    
    args = sys.argv[1:]

    # Check if user passed arguments
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)
    verbose = "--verbose" in args

    messages = types.Content(role="user", parts=[types.Part(text=user_prompt)])

    # Provide API key 
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    response = client.models.generate_content(
        # model="gemini-2.0-flash-001", 
        model="gemini-2.5-flash", 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    function_call_results = []

    print("Response:")

    for function_call in response.function_calls:

        function_call_result = call_function(function_call, verbose)

        parts = function_call_result.parts
        if not parts:
            raise Exception("No parts returned by function: call_function()")
        
        fr = function_call_result.parts[0].function_response
        if fr is None or fr.response is None:
            raise Exception("No function_response/response returned by call_function()")

        function_call_results.append(function_call_result.parts[0])
        
        if verbose:
            print(f"-> {fr.response}")

if __name__ == "__main__":
    main()
