number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = str(input("Enter + - * /: "))
if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
