# assignment: programming assignment 3
# author: Diana Martinez
# date: 11/16/2020
# file: calculator.py is a program that emulates a simple calculator that can
#       add, subtract, multiply or divide two numbers
# input: Strings, Integers, floats
# output: Integers, floats, strings

def format(num, precision=2):
    return str(round(num, precision)).strip("0")


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def isfloat(token):
    dot = False
    minus = False
    for char in token:
        if char.isdigit():  # allow many digits in a string
            continue
        elif char == ".":  # allow only one dot in a string
            if not dot:
                dot = True
            else:
                return False
        elif char == "-" and token[0] == "-":  # allow one minus in front
            if not minus:
                minus = True
            else:
                return False
        else:  # do not allow any other characters in a string
            return False
    return True


print("Welcome to Calculator Program!")
programRun = True
while programRun:
    checkCorrectInput = True
    while checkCorrectInput:
        userInput = input("Please choose one of the following operations:"
                          "\nAddition - A\nSubtraction - S\nMultiplication - M\nDivision - D\n> ")
        if userInput in "ASMD":
            checkCorrectInput = False
        else:
            print("You did not choose correctly.")

    correctNum1 = True
    while correctNum1:
        num1 = input("Please enter the first number: ")
        if isfloat(num1):
            correctNum1 = False
        else:
            print("You did not choose a number.")

    correctNum2 = True
    print("The first number is " + num1)
    while correctNum2:
        num2 = input("PLease enter the second number: ")
        if isfloat(num2):
            correctNum2 = False
        else:
            print("You did not choose a number.")
    print("The second number is " + num2)

    if userInput == "A":  # chose addition
        sum = add(float(num1), float(num2))
        print(num1 + " + " + num2 + " = " + format(sum, 2))

    if userInput == "S":  # chose subtraction
        sub = subtract(float(num1), float(num2))
        print(num1 + " - " + num2 + " = " + format(sub))

    if userInput == "M":  # chose multiplication
        mult = multiply(float(num2), float(num2))
        print(num1 + " * " + num2 + " = " + format(mult))

    if userInput == "D":  # chose division
        div = divide(float(num1), float(num2))
        print(num1 + " / " + num2 + " = " + format(div))

    askEndBoolean = True
    while askEndBoolean:
        askEndGame = input("Do you want to continue? [Y/N]: ")
        if askEndGame == "Y":
            programRun = True
            askEndBoolean = False
        elif askEndGame == "N":
            print("Goodbye!")
            programRun = False
            askEndBoolean = False
        else:
            print("You did not choose correctly.")
