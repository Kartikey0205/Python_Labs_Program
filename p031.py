# WAP to Remove multiple elements from a list in Python
# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    list1.append(ele)

print("Elements in the list are as follows: ", list1)
unwanted = []
# asking number of elements to remove from list
x = int(input("Enter number of elements to remove: "))

for i in range(1, x + 1):
    item = int(input("Enter elements: "))
    unwanted.append(item)

for ele in list1:
    if ele in unwanted:
        list1.remove(ele)

# printing modified list
print("New list after removing unwanted elements: ", list1)

"""
OUTPUT:
Enter number of elements in list: 8
Enter elements: 1
Enter elements: 2
Enter elements: 7
Enter elements: 4
Enter elements: 9
Enter elements: 5
Enter elements: 0
Enter elements: 3
Elements in the list are as follows:  [1, 2, 7, 4, 9, 5, 0, 3]
Enter number of elements to remove: 2
Enter elements: 5
Enter elements: 8
New list after removing unwanted elements:  [1, 2, 7, 4, 9, 0, 3]
"""