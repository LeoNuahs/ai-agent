import subprocess
import os
from google.genai import types

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

        if completed_process.stdout:
            output.append(f"STDOUT: \n{completed_process.stdout}")

        if completed_process.stderr:
            output.append(f"STDERR: \n{completed_process.stderr}")

        if completed_process.returncode != 0:
            output.append(f"Process exited with code \"{completed_process.returncode}\"")

        if output:
            return "\n".join(output)
        else:
            return "No output produced."

    except Exception as e:
        return f"Error: executing Python file: \"{e}\""

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the specified python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read the contents of, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY, 
                items=types.Schema(
                    type=types.Type.STRING, 
                    description="Optional arguments to pass to the Python file.", 
                ), 
                description="Optional arguments to pass to the Python file.", 
            )
        },
        required=["file_path"], 
    ),
)
