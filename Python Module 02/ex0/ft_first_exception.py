#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    try:
        return int(temp_str)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return (0)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    value = input_temperature('25')
    if (value != 0):
        print(f"Temperature is now {value}")
    print("")
    print("Input data is 'abc'")
    value = input_temperature('abc')
    if (value != 0):
        print(f"Temperature is now {value}")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
