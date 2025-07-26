from functions.get_files_info import get_files_info
from functions.get_file_contents import get_file_content

def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)

    result = get_files_info("calculator", "main.py")
    print("Result for 'main.py' file:")
    print(result)

    result = get_files_info("calculator", "lorem.txt")
    print("Contents of lorem.txt:")
    print(result)

    result = get_files_info("calculator", "main.py")
    print("Contents of calculator/main.py:")
    print(result)

    result = get_files_info("calculator", "pkg/calculator.py")
    print("Contents of calculator/pkg/calculator.py:")
    print(result)

    result = get_files_info("calculator", "/bin/cat")
    print("Contents of /bin/cat:")
    print(result)

    result = get_files_info("calculator", "pkg/does_not_exist.py")
    print("Contents of calculator/pkg/does_not_exist.py:")
    print(result)

if __name__ == "__main__":
    test()
