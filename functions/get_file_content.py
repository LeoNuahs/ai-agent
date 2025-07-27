import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    permitted_dir = os.path.abspath(working_directory)

    input_file = os.path.join(working_directory, file_path)
    target_file = os.path.abspath(input_file)

    if not target_file.startswith(permitted_dir):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.isfile(target_file):
        return f"Error: File not found or is not a regular file: \"{file_path}\""

    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            
            if os.path.getsize(target_file) > MAX_CHARS:
                file_content_string += f"\n\n[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"

            return file_content_string
    except Exception as e:
        return f"Error reading file {file_path}: {e}"

