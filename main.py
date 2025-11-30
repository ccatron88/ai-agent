import os
import sys
from dotenv import load_dotenv
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

    messages = types.Content(role="user", parts=[types.Part(text=user_prompt)])

    # Provide API key 
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # client = genai.Client(
    #     vertexai=True, project='Boot-dev Ai Agent', location='us-central1'
    # )   
    
    # response = client.models.generate_content(
    #     model=model_name,
    #     contents=messages,
    # )
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    print("Response:")
    print(response.text)
    if '--verbose' in args:
        print("User prompt:", user_prompt)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)


if __name__ == "__main__":
    main()
