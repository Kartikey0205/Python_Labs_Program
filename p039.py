# WAP of recursive function to calculate sum of numbers from 0 to 10
def sum(n):
    if n == 1:
        return n
    s = n + sum(n - 1)
    return s


num = 10
print("Sum of numbers from 0 to 10 ", sum(num))
"""
OUTPUT:
Sum of numbers from 0 to 10  55
"""