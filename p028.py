# WAP to find smallest number in a list

# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
    el = int(input("Enter elements: "))
    list1.append(el)

# print smallest element
print("Your list is : ", list1)
print("Smallest element in list1 is:", min(list1))

"""
OUTPUT:
Enter number of elements in list: 5
Enter elements: 1
Enter elements: 2
Enter elements: 7
Enter elements: 3
Enter elements: 9
Your list is :  [1, 2, 7, 3, 9]
Smallest element in list1 is: 1
"""