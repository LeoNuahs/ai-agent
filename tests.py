from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test_get_files_info():
    result = get_files_info("calculator", ".")
    print("\nResult for current directory:")
    print(result)

    result = get_files_info("calculator", "pkg")
    print("\nResult for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("\nResult for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("\nResult for '../' directory:")
    print(result)

    result = get_files_info("calculator", "main.py")
    print("\nResult for 'main.py' file:")
    print(result)

def test_get_file_content():
    # result = get_file_content("calculator", "lorem.txt")
    # print("\nContents of lorem.txt:")
    # print(result)

    result = get_file_content("calculator", "main.py")
    print("\nContents of calculator/main.py:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("\nContents of calculator/pkg/calculator.py:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("\nContents of /bin/cat:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("\nContents of calculator/pkg/does_not_exist.py:")
    print(result)

def test_write_file():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("\nContents of calculator/lorem.txt:")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("\nContents of calculator/pkg/morelorem.txt:")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("\nContents of calculator/tmp/temp.txt:")
    print(result)


if __name__ == "__main__":
    # test_get_files_info()
    # test_get_file_content()
    test_write_file()
