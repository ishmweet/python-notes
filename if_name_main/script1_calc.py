def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(__name__)
if __name__ == "__main__":  # by adding this, it will only run here and not in script2
    print("This is a simple calculator.")
    print()
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print()
    print(f"The sum is: {add(num1, num2)}")
    print(f"The difference is: {subtract(num1, num2)}")
    