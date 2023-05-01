firstNum = int(input("First number: "))
secondNum = int(input("Second number: "))
sign = input("Choose the sign(+, - , * /: ")

if sign == '+':
    print("Result: ", firstNum + secondNum)
elif sign == '-':
    print("Result: ", firstNum - secondNum)
elif sign == '*':
    print("Result: ", firstNum * secondNum)
elif sign == '/':
    print("Result: ", firstNum / secondNum)