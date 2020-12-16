"""
WAP to generate a dictionary that contains numbers ranging from 1 to n as keys
and the values are cube of keys. Prompt the user to enter the value of n.
"""

n = int(input("Enter a number "))
d = dict()
for X in range(1, n + 1):
    d[X] = X * X * X
print(d)

"""
Enter a number 6
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}
"""