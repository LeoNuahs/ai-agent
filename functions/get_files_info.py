import os

def get_files_info(working_directory, directory="."):
    permitted_dir = os.path.abspath(working_directory)

    input_dir = os.path.join(working_directory, directory)
    target_dir = os.path.abspath(input_dir)

    if not target_dir.startswith(permitted_dir):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"

    if not os.path.isdir(target_dir):
        return f"Error: \"{directory}\" is not a directory"

    try:
        files_info = []
        files = os.listdir(target_dir)
        print(files)
        for file in files:
            file_path = os.path.join(target_dir, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)

            files_info.append(f" - {file}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
