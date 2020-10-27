# assignment: programming assignment 1
# author: Diana Martinez
# date: (10/05/2020) October 5, 2020
# file: hello.py is a program that asks the user to enter user’s name,
#       age, and favorite movie and outputs a greeting message that
#       include the information about the user
# input: string data
# output: string data
username = str(input("Hello! What is your name?"))
# casting to int because that is what is asked for in rubric
hello_ = int(input("What is your age?"))
favorite_movie = str(input("What is your favorite movie?"))
print("Nice to meet you, " + username)
print("You are " + str(hello_) + " years old and your favorite movie is " + favorite_movie + ".")
