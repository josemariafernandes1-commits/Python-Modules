#!/usr/bin/env python3


def secure_archive(filename: str, action: str = 'r',
                   filecontent: str = "") -> tuple[bool, str]:
    try:
        if action == 'r':
            with open(filename, 'r') as file:
                content = file.read()
                return (True, content)
        elif action == 'w':
            with open(filename, 'w') as file:
                file.write(filecontent)
                return (True, f"Content successfully written to {filename}")
        else:
            return (False, f"Invalid operation: {action}")
    except FileNotFoundError as e:
        return (False, f"{e}")
    except PermissionError as e:
        return (False, f"{e}")


def test_secure_archive() -> None:
    print("=== Cyber Archives Security ===\n")
    test1 = "not_existant.txt"
    print(f"Using '{secure_archive.__name__}' "
          "to read from a nonexistent file:")
    result1 = secure_archive(test1)
    print(result1)
    print()
    test2 = "noread.txt"
    print(f"Using '{secure_archive.__name__}' "
          "to read from an inaccessible file:")
    result2 = secure_archive(test2)
    print(result2)
    print()
    test3 = "ancient_fragment.txt"
    print(f"Using '{secure_archive.__name__}' to read from a regular file:")
    result3 = secure_archive(test3)
    print(result3)
    print()
    test4 = "newfile.txt"
    print(f"Using '{secure_archive.__name__}' "
          "to write previous content to a new file:")
    result4 = secure_archive(test4, "w", result3[1])
    print(result4)
    # print()
    # test5 = "newfile2.txt"
    # print(f"Using '{secure_archive.__name__}' "
    #       "to test for incorrect operations:")
    # result5 = secure_archive(test5, "x", result3[1])
    # print(result5)


if __name__ == '__main__':
    test_secure_archive()
