def divide(a, b):
    # Check for division by zero
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a / b  # Regular division

# Example usage:
result = divide(10, 2)
print(result)  # Output: 5.0

result = divide(10, 0)
print(result)