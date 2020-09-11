#  WAP to calculate distance between two points

x1 = int(input("Enter x-cordinate of first point "))
y1 = int(input("Enter y-cordinate of first point "))
print("First point is :", (x1, y1))
x2 = int(input("Enter x-cordinate of second point "))
y2 = int(input("Enter y-cordinate of second point "))
print("Second point is :", (x2, y2))
d = (((x2 - x1) ** 2) - ((y2 - y1) ** 2)) ** (0.5)
print("The distance between two points are: ", d)

"""
OUTPUT:
Enter x-cordinate of first point 2
Enter y-cordinate of first point 6
First point is : (2, 6)
Enter x-cordinate of second point 8
Enter y-cordinate of second point 4
Second point is : (8, 4)
The distance between two points are:  5.656854249492381
"""
