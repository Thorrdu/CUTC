import os
import base64
from pathlib import Path

# Define supported image and text extensions
IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']
TEXT_EXTENSIONS = ['.txt', '.py', '.js', '.ts', '.md', '.html', '.css', '.json', '.xml', '.yaml', '.yml']

def is_image_file(path):
    return path.suffix.lower() in IMAGE_EXTENSIONS

def is_text_file(path):
    return path.suffix.lower() in TEXT_EXTENSIONS

def process_input(user_input):
    """Processes user input, handling file paths for images and text."""
    try:
        input_path = Path(user_input)
        if input_path.is_file():
            if is_image_file(input_path):
                # It's an image, encode it in base64
                with open(input_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                print(f"IMAGE_CONTEXT_START:{input_path.name}::{encoded_string}:IMAGE_CONTEXT_END")
            elif is_text_file(input_path):
                # It's a text file, print its content
                with open(input_path, "r", encoding='utf-8', errors='ignore') as text_file:
                    content = text_file.read()
                print(f"FILE_CONTEXT_START:{input_path.name}::{content}:FILE_CONTEXT_END")
            else:
                # It's another type of file, treat as a text prompt
                print(user_input)
        else:
            # It's not a valid file path, treat as a text prompt
            print(user_input)
    except Exception:
        # Handle cases where input is not a valid path at all
        print(user_input)

if __name__ == "__main__":
    prompt_text = input("prompt (or file path): ")
    if prompt_text.lower() == 'stop':
        print("stop")
    else:
        process_input(prompt_text) 