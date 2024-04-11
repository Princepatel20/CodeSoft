def calculator():
    # Get user input
    num1 = float(input("Enter the first number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the calculation
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation.")

    # Display the result
    if result is not None:
        print(f"{num1} {operation} {num2} = {result}")

# Run the calculator
calculator()
