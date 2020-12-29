"""
WAP to check the validity of a password given by the user using
regular expressions. The Password should satisfy the following criteria:
a) Contain at least 1 letter between a and z
b) Contain at least 1 number between 0 and 9
c) Contain at least 1 letter between A and Z
d) Contain at least 1 character from $, #, _, @
e) Minimum length of password: 8
f) Maximum length of password: 20
"""
import re
password = input("Enter the password ")
flag=0
while True:
    if (len(password)<8):
        flag=-1
        break
    elif not re.search("[a-z]",password):
        flag=-1
        break
    elif not re.search("[A-Z]",password):
        flag=-1
        break
    elif not re.search("[0-9]", password):
        flag = -1
        break
    elif not re.search("[_@$]", password):
        flag = -1
        break
    elif re.search("\s", password):
        flag = -1
        break
    else:
        flag=0
        print("Valid Password")
        break
    if flag == -1:
        print("Not a Valid Password")

"""
Output:
Enter the password Hello@990
Valid Password

"""