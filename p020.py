# WAP to Reverse a given number and return true if it is the same as the original number.
num = int(input("Enter a number : "))
r = 0
temp = num
while num != 0:
    a = num % 10
    r = r * 10 + a
    num = num // 10
print("Reverse is : ", r)
if r == temp:
    print("True , Reverse number is equal to original number ")
else:
    print("False , Reverse number is not equal to original number ")

"""
OUTPUT:
Enter a number : 1221
Reverse is :  1221
True , Reverse number is equal to original number 
"""