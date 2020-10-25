"""
Print downward Half-Pyramid Pattern with Star (asterisk)

* * * *
* * *
* *
*
"""
for rows in range(4, 0, -1):
    print()
    for columns in range(1, rows + 1):
        print("*", end=" ")

"""
OUTPUT:

* * * * 
* * * 
* * 
* 
"""