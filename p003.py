# WAP to calculate area of triangle by Heron's Formula

a = int(input("Enter the first sides of Triangle "))
b = int(input("Enter the second sides of Triangle "))
c = int(input("Enter the third sides of Triangle "))
S = (a + b + c) / 2
area = (S * (S - a) * (S - b) * (S - c)) ** (0.5)
print("Area of Triangle using Heron's Formula is : ", area)

"""
OUTPUT:
Enter the first sides of Triangle 20
Enter the second sides of Triangle 12
Enter the third sides of Triangle 16
Area of Triangle using Heron's Formula is :  96.0

"""
