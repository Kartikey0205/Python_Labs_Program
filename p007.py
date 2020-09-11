# WAP to demonstrate the use of Relational Operators

a = int(input("Enter the first  number "))
b = int(input("Enter the second number "))
print("Let's see the use of RELATIONAL OPERATOR")
r1 = (a == b)
print("Is a==b ->", r1)
r2 = (a != b)
print("Is a!=b ->", r2)
r3 = (a > b)
print("Is a>b ->", r3)
r4 = (a < b)
print("Is a<b ->", r4)
r5 = (a >= b)
print("Is a>=b ->", r5)
r6 = (a <= b)
print("Is a<=b ->", r6)

"""
OUTPUT:
Enter the first  number 76
Enter the second number 98
Let's see the use of RELATIONAL OPERATOR
Is a==b -> False
Is a!=b -> True
Is a>b -> False
Is a<b -> True
Is a>=b -> False
Is a<=b -> True
"""