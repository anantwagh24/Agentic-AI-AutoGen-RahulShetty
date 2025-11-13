# Program to reverse a string without using built-in functions
def string_reverse():

    str=input("enter a string to reverse: ")

    str=str.lower()

    for i in range(len(str)-1, -1, -1):
        print(str[i], end=" ")

string_reverse()