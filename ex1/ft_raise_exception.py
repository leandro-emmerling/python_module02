#!/usr/bin/python3


def input_temperature(temp_str: str) -> int:
    """Convert temperature string to int and validate range (0-40°C)."""
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp} is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp} is too hot for plants (max 40°C)")
    return (temp)


def test_temperature() -> None:
    """Test input_temperature with valid and invalid inputs."""
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
    print()
    print("Input data is '100'")
    try:
        result = input_temperature("100")
        print(f"Temperature is now {result}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")
    print()
    print("Input data is '-50'")
    try:
        result = input_temperature("-50")
        print(f"Temperature is now {result}°C")
    except ValueError as err:
        print(f"Caught input_temperature error: {err}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
