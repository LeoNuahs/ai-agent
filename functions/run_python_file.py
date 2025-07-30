import subprocess
import os

def run_python_file(working_directory, file_path, args=[]):
    permitted_dir = os.path.abspath(working_directory)

    input_dir = os.path.join(working_directory, file_path)
    target_file = os.path.abspath(input_dir)

    if not target_file.startswith(permitted_dir):
        return f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory"

    if not os.path.exists(target_file):
        return f"Error: File \"{file_path}\" not found."

    if not target_file.endswith(".py"):
        return f"Error: \"{file_path}\" is not a Python file."

    command = ["python", target_file]
    if args:
        command.extend(args)

    try:
        completed_process = subprocess.run(
            command, 
            capture_output=True, 
            timeout=30, 
            text=True,
            cwd=permitted_dir, 
        )

        output = []

        if completed_process.returncode != 0:
            return f"Process exited with code \"{completed_process.returncode}\""

        if not completed_process.stdout:
            return "No output produced."
        else:
            output.append(f"STDOUT: \n{completed_process.stdout}")

        if completed_process.stderr:
            output.append(f"STDERR: \n{completed_process.stderr}")

        return output
    except Exception as e:
        return f"Error: executing Python file: \"{e}\""
