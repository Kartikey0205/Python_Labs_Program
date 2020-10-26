# WAP to print sum of all the numbers in a list.

list1 = []
total = int(input("Enter the total numbers of list : "))

for i in range(1, total + 1):
    ele = int(input("Enter elements : "))
    list1.append(ele)
print("Your List is : ", list1)
sum = 0
for ele in list1:
    sum = sum + ele

print("Value of addition of each and every item of list is : ", sum)
"""
OUTPUT:
Enter the total numbers of list : 5
Enter elements : 35
Enter elements : 9
Enter elements : 2
Enter elements : 70
Enter elements : 25
Your List is :  [35, 9, 2, 70, 25]
Value of addition of each and every item of list is :  141
"""