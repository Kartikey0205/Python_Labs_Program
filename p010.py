# WAP to calculate average of 2 numbers and its deviation
a = int(input("Enter the first  number "))
b = int(input("Enter the second  number "))
avg = (a + b) / 2
print("The average of ", a, "and", b, "is ", avg)
print("The deviation of average from first number is : ", avg - a)
print("The deviation of average from second number is : ", avg - b)

"""
OUTPUT:
Enter the first  number 56
Enter the second  number 39
The average of  56 and 39 is  47.5
The deviation of average from first number is :  -8.5
The deviation of average from second number is :  8.5

"""