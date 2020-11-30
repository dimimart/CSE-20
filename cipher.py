# assignment: programming assignment 4
# author: Diana Martinez
# date: 11/30/2020
# file: cipher.py is a program where you can implement a simple encoder-decoder program that uses a Caesar cipher.
# input: text files (messages)
# output: strings (of decoded or encoded files)

# function to read a file
def readfile(filename):
    message = ""
    f = open(filename, "r")
    # read from file
    message = f.read()
    f.close()
    return message


# function to write in file
def writefile(filename, message):
    f = open(filename, "w")
    f.write(message)
    f.close()


# to create a tuple of alphabets
def make_alphabet():
    alphabet = ()
    for index in range(26):
        char = index + 65
        alphabet += (chr(char),)
    return alphabet


# encode function
def encode(plaintext):
    shift = 3
    ciphertext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in plaintext:
        found = False
        for i in range(length):
            if char == alphabet[i]:
                letter = alphabet[(i + shift) % length]
                ciphertext.append(letter)
                found = True
                break
        if not found:
            ciphertext.append(char)
    return ciphertext


# decode function
def decode(text):
    shift = -3
    plaintext = []
    alphabet = make_alphabet()
    length = len(alphabet)
    for char in text:
        found = False
        for index in range(length):
            if char == alphabet[index]:
                j = index + shift
                if j < 0:
                    j = j + 26
                letter = alphabet[j % length]
                plaintext.append(letter)
                found = True
                break
        if not found:
            plaintext.append(char)
    return plaintext


# function to convert list in string
def to_string(text):
    s = ""
    for index in text:
        s += index
    return s


# main program
def main():
    print("Would you like to encode or decode the message")
    userInput = input("Type E to encode D to decode Q to quit: ")
    while True:
        if userInput == 'E':
            filename = input("Please enter a file for reading: ")
            text = readfile(filename)
            filename = input("Please enter a file for writing: ")
            print("plaintext:")
            print(text)
            textVar = encode(text)
            textToString = to_string(textVar)
            print("ciphertext: ")
            print(textToString)
            writefile(filename, textToString)
        elif userInput == 'D':
            filename = input("Please enter a file for reading: ")
            text = readfile(filename)
            filename = input("Please enter a file for writing: ")
            print("ciphertext: " + text)
            textVar = decode(text)
            textToString = to_string(textVar)
            print("plaintext: " + textToString)
            writefile(filename, textToString)
        elif userInput == 'Q':
            print("Goodbye!")
            break
        else:
            print("Wrong Input!")
        print("Would you like to encode or decode the message")
        userInput = input("Type E to encode D to decode Q to quit: ")


main()