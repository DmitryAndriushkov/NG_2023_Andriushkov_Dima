def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: division by zero"
    else:
        return x / y
print("==============================================")
print("Welcome to my calculator V2.0!\n")
print("1) Addition")
print("2) Substraction")
print("3) Multiplication")
print("4) Division")

choice = input("\nChoose the operation (1/2/3/4): ")
print("==============================================")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

if choice == '1':
    print("==============================================")

    print("Result: ",num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print("==============================================")

    print("Result: ",num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print("==============================================")

    print("Result: ",num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print("==============================================")

    print("Result: ",num1, "/", num2, "=", divide(num1, num2))

else:
    print("==============================================")
    print("Incorrect input!!!")
print("==============================================")
