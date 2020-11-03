# Write a function calculation() such that it can accept two variables
# and calculate their addition and subtraction. And also it must return
# both addition and subtraction in a single return call

def calculation(a, b):
    sum = a + b
    diff = a - b
    return sum, diff


n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))

add, sub = calculation(n1, n2)
print("Addition of two numbers are : ", add)
print("Subtraction of two numbers are : ", sub)

"""
OUTPUT:
Enter first number 50
Enter second number 20
Addition of two numbers are :  70
Subtraction of two numbers are :  30

"""