# WAP to demonstrate class Methods as Alternative Constructors in Python.

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # This method is used for not passing so many values in different way just pass one string and then instead of
    # going in __init__ constructor it goes to new method
    @classmethod
    def from_dash(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


rohan = Employee("Rohan", 455, "Student")
print(rohan.salary)
Kartikey = Employee.from_dash("Kartikey-800000000-Web Developer")
print(Kartikey.salary)

#OUTPUT-
# 455
# 800000000
