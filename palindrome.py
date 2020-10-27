#part of lab 5

#A palindrome is a word, phrase, or sequence that reads the same backward as forward.
#Write a code snippet that asks the user to enter a palindrome (“Please, enter a palindrome: ”)
#and verifies if the word x entered by the user is a palindrome (“The word x is a palindrome.”
#or “The word x is not a palindrome.”; x should be substituted to its value).

userInput = input("Please, enter a palindrome: ")
if userInput == userInput[::-1]:
    print("The word " + userInput + " is a palindrome.")
else:
    print("The word " + userInput + " is not a palindrome.")
