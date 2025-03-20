def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Result:", subtract(num1, num2))
