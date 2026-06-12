# Write a code for a simple calculator in python that can perform basic arithmetic operations like addition, subtraction, multiplication, and division. The calculator should take two numbers and an operator as input from the user and display the result of the operation.

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError("Unsupported operator. Use +, -, *, or /." )

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def get_operator():
    valid_operators = {"+", "-", "*", "/"}
    while True:
        op = input("Enter an operator (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        print("Invalid operator. Please enter one of +, -, *, /.")


def main():
    print("Simple Calculator")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")
    operator = get_operator()

    try:
        result = calculate(a, b, operator)
        print(f"Result: {a} {operator} {b} = {result}")
    except ZeroDivisionError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)


if __name__ == "__main__":
    main()
