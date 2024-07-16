
# Menu driven program to perform arithmetic operations

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "5":
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    try:
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("Invalid choice. Please try again.")
            continue

        print(f"Result: {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
