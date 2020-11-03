# Write a python function that checks whether a passed string is palindrome or not.


def check(st):
    if st == st[::-1]:
        print("The passed string is a palindrome ")

    else:
        print("The passed string is not a palindrome ")


s = input("Enter a string : ")
check(s)
"""
OUTPUT:
Enter a string : racecar
The passed string is a palindrome 
"""