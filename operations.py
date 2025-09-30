def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("=== Addition and Subtraction ===")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")

if _name_ == "_main_":
    main()
