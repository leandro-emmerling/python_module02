#!/usr/bin/python3


def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        result = input_temperature("25")
        print(f"Temperature is now {result}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print()
    print("Input data is 'abc'")
    try:
        result = input_temperature("abc")
        print(f"Temperature is now {result}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
