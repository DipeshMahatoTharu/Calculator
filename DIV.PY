def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input. Please enter numbers."

# Example usage
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Result:", divide(num1, num2))
