# Step 1: Ask the user to enter the first number
num1 = float(input("Enter the first number: "))

# Step 2: Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Step 3: Ask the user to choose an operation
operation = input("Enter an operation (+, -, *, /): ")

# Step 4: Perform the chosen operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid operation. Please enter +, -, *, or /.")

