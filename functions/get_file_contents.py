import os

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
            return f
    except Exception as e:
        return f"Error reading file: {e}"

