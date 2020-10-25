"""
Print the following pattern using for loop

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""

for rows in range(5, 0, -1):
    print()
    for columns in range(rows, 0, -1):
        print(columns, end=" ")
    # print()

"""
Output:

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""