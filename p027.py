# Count all lower case, upper case, digits, and special symbols from a given string
str = input("Enter any String ")
lowerValue = 0
upperValue = 0
digitValue = 0
specialValue = 0

for i in str:
    if i.islower():
        lowerValue += 1
    elif i.isupper():
        upperValue += 1
    elif i.isdigit():
        digitValue += 1
    else:
        specialValue += 1
print("Total number of counts of  lower case of entered string is : ", lowerValue)
print("Total number of counts of  upper case of entered string is : ", upperValue)
print("Total number of counts of  digits of entered string is : ", digitValue)
print("Total number of counts of  special symbols of entered string is : ", specialValue)

"""
OUTPUT:
Enter any String Howare_you1929@gmail.com
Total number of counts of  lower case of entered string is :  16
Total number of counts of  upper case of entered string is :  1
Total number of counts of  digits of entered string is :  4
Total number of counts of  special symbols of entered string is :  3

"""