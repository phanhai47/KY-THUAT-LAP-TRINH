print("Sinh vien : Phan Dinh Hai")
print("245752021610016")
print("##################################")

import math

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

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid choice! Please select a number from 1 to 4.")
