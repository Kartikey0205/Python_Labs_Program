# Create a function showEmployee() in such a way that it should
# accept employee name, and it’s salary and display both, and if the
# salary is missing in function call it should show it as 9000

def showEmployee(name, salary=9000):
    print("Employee name is : ", name)
    print("Salary of Employee is : Rs.", salary)


user_name = input("Enter your name : ")
user_salary = int(input("Enter your  Salary : "))
print("\nWhen salary is  pass as argument in function call ")
showEmployee(name=user_name, salary=user_salary)
print("\nWhen salary is not pass as argument in function call ")
showEmployee(name=user_name)

"""
OUTPUT:
Enter your name : Kartikey
Enter your  Salary : 20000000

When salary is  pass as argument in function call 
Employee name is :  Kartikey
Salary of Employee is : Rs. 20000000

When salary is not pass as argument in function call 
Employee name is :  Kartikey
Salary of Employee is : Rs. 9000
"""
