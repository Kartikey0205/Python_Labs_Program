# WAP  to sort (ascending and descending) a dictionary by value.
myDic = {1: 32, 2: 46, 3: 3, 4: 9, 5: 30, 6: 99}
print("Original Dictionary : ", myDic)
asc = sorted(myDic.values())
print("Dictionary by value in ascending order is : ", asc)
print("Dictionary by value in descending order is : ", asc[::-1])

"""
OUTPUT:
Original Dictionary :  {1: 32, 2: 46, 3: 3, 4: 9, 5: 30, 6: 99}
Dictionary by value in ascending order is :  [3, 9, 30, 32, 46, 99]
Dictionary by value in descending order is :  [99, 46, 32, 30, 9, 3]
"""