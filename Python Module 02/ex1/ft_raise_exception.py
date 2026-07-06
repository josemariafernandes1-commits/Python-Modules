#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    return int(temp)


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    print("Input data is '25'")
    try:
        value = input_temperature('25')
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    print("Input data is 'abc'")
    try:
        value = input_temperature('abc')
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    print("Input data is '100'")
    try:
        value = input_temperature('100')
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    print("Input data is '-50'")
    try:
        value = input_temperature('-50')
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()
