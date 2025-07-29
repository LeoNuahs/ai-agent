import os

def write_file(working_directory, file_path, content):
    permitted_dir = os.path.abspath(working_directory)

    input_dir = os.path.join(working_directory, file_path)
    target_file = os.path.abspath(input_dir)

    if not target_file.startswith(permitted_dir):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.isfile(target_file):
        return f"Error: {file_path} is not a file"

    target_dir = os.path.dirname(target_file)

    if not os.path.exists(target_file):
        try:
            os.makedirs(target_dir, exist_ok=True)
        except Exception as e:
            return f"Error: Cannot create directory {target_dir}: {e}"

    try:
        with open(target_file, "w") as f:
            f.write(content)

        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: Cannot write to file {file_path}: {e}"
