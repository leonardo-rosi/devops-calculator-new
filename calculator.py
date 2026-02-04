from operations import add, subtract, multiply, divide

def calculate(operation: str, a: float, b: float) -> float:
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        raise ValueError("Invalid operation. Supported operations are: add, subtract, multiply, divide.")
    
# Example usage:
if __name__ == "__main__":
    print(calculate("add", 5, 3))        # Output: 8
    print(calculate("subtract", 5, 3))   # Output: 2
    print(calculate("multiply", 5, 3))   # Output: 15
    print(calculate("divide", 6, 3))     # Output: 2.0
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    print("Sum of ", x, " and ", y, " is ", calculate("add", float(x), float(y)))
    print("Difference of ", x, " and ", y, " is ", calculate("subtract", float(x), float(y)))
    