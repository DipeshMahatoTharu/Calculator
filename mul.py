def multiply(x, y):
    return x * y

while True:
    print("\nMultiplication Calculator")
    print("Enter two numbers to multiply or type 'exit' to quit.")

    num1 = input("Enter first number: ")
    if num1.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    num2 = input("Enter second number: ")
    if num2.lower() == 'exit':
        print("Exiting calculator. Goodbye!")
        break

    try:
        num1 = float(num1)
        num2 = float(num2)
        result = multiply(num1, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers!")
