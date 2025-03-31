'''*****************************************************
* Name    : Calculator.py
* Purpose : To perform simple mathematical operations
* Author  : Navin Chakravarthy Kamalakannan
*********************************************************'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    operations = [add,subtract,multiply,divide]

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {operations[int(choice)-1](num1,num2)}")
        except ValueError:
            print("Invalid input! Please enter a number.")

    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
