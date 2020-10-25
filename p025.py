# WAP of loop to find the factorial of any number
num = int(input("Enter a number: "))
factorial = 1

for i in range(num, 0, -1):
    factorial = factorial * i
print("Factorial of ", num, " is : ", factorial)

"""
OUTPUT:
Enter a number: 7
Factorial of  7  is :  5040
"""