# Given a string of odd length greater 7, return a string made of the middle three chars of a given String

stri = input("Enter any string whose length is greater than 7 ")
if len(stri) > 7:
    check = len(stri)
    if check % 2 != 0:
        # print(check)
        print("String made by Middle 3 chars of entered string is ")
        print(stri[(check // 2) - 1:((check // 2) + 2)])
    else:
        print("You entered string greater than  length of 7 but entered a even length string ")

else:
    print("Sorry , INVALID String , You entered string less than length of 7")

"""
OUTPUT:
Enter any string whose length is greater than 7 Hello, Good Morning Kartikey , How are you Kartikey
String made by Middle 3 chars of entered string is 
ike
"""
