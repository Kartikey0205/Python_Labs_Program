# WAP of recursive function to calculate factorial of numbers
def factorial(n):
    if n <= 1:
        return 1
    s = n * factorial(n - 1)
    return s


num = int(input("Enter a number : "))

f = factorial(num)
print("Factorial of number is : ", f)

"""
OUTPUT:

Enter a number : 7
Factorial of number is :  5040
"""