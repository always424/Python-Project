# Python Calculator

operation = input("What Operation Do U Want (+ - * /) : ")

number1 = float(input("What is the first number : "))
number2 = float(input("What is the second number : "))

if operation == "+":
    res = number1 + number2
    print(f"The result is {res}")

elif operation == "-":
    res = number1 - number2
    print(f"The result is {res}")


elif operation == "*":
    res = number1 * number2
    print(f"The result is {res}")

else:
    res = number1 * number2
    print(f"The result is {res}")
