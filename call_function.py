from google.genai import types

from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from config import WORKING_DIR

def call_function(call, verbose=False):
    function_name = call.name
    function_args = call.args

    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map = {
            "get_files_info": get_files_info, 
            "get_file_content": get_file_content, 
            "run_python_file": run_python_file, 
            "write_file": write_file
    }

    function_args["working_directory"] = WORKING_DIR

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=call.name,
                    response={"error": f"Unknown function: {call.name}"},
                )
            ],
        )

    # call function and return a types.Content with a from_function_response that describes output
    function_result = function_map[function_name](**function_args)
    return types.Content(
        role="tool", 
        parts=[
            types.Part.from_function_response(
                name=function_name, 
                response={"result": function_result}
            )
        ]
    )

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content, 
        schema_run_python_file, 
        schema_write_file, 
    ]
)
