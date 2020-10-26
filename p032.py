# WAP  to multiply all the items in a list.
list1 = []
total = int(input("Enter the total numbers of list : "))

for i in range(1, total + 1):
    ele = int(input("Enter elements : "))
    list1.append(ele)
print("Your List is : ", list1)
mul = 1
for ele in list1:
    mul = mul * ele

print("Value of Multiplication of each and every item of list is : ", mul)
"""
OUTPUT:
Enter the total numbers of list : 5
Enter elements : 1
Enter elements : 2
Enter elements : 3
Enter elements : 4
Enter elements : 5
Your List is :  [1, 2, 3, 4, 5]
Value of Multiplication of each and every item of list is :  120
"""