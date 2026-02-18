"""
Project: Python CLI Arithmetic Calculator
Author: Rumi
Description:
A command-line calculator that performs basic arithmetic
operations with proper input validation and error handling.
"""

def calculate(num1: float, num2: float, operator: str):
    """
    Perform arithmetic operation based on the operator provided.
    """

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2

    elif operator == "//":
        if num2 == 0:
            return "Error: Floor division by zero is not allowed."
        return num1 // num2

    elif operator == "%":
        if num2 == 0:
            return "Error: Modulus by zero is not allowed."
        return num1 % num2

    else:
        return "Error: Invalid operator."


def main():
    """
    Main function to execute the calculator program.
    """

    print("\n=== Python CLI Arithmetic Calculator ===\n")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, //, %): ").strip()

        result = calculate(num1, num2, operator)
        print(f"\nResult: {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")


if __name__ == "__main__":
    main()
