# WAP of  two integer numbers which return their  product and if the product is greater than 1000, then return their sum

first = int(input("Enter First Number "))
second = int(input("Enter Second Number "))
product = first * second
sum = first + second
if product > 1000:
    print("Sum of ", first, " and ", second, " is : ", sum)
else:
    print("Product of ", first, " and ", second, " is : ", product)

"""
OUTPUT:
Enter First Number 100
Enter Second Number 20
Sum of  100  and  20  is :  120
"""
