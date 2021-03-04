# WAP to show the use of self and init (constructors) in Python.
# Class related to self
class Student:
    no_of_leaves_granted = 8

    def printDetails(self):  # self uss object ko point krega jiski baat ho rhi h
        return f"Name of Student is {self.name},Section is {self.Section}, Course is {self.Course}, " \
               f"and Roll number is {self.Roll_no} "


Kartikey = Student()
Vanya = Student()

Kartikey.name = "Kartikey Dubey"
Kartikey.Section = "A"
Kartikey.Course = "B.Tech"
Kartikey.Roll_no = 15

Vanya.name = "Vanya Tripathi"
Vanya.Section = "A"
Vanya.Course = "SKG"
Vanya.Roll_no = 1

print(Vanya.printDetails())
print(Kartikey.printDetails())


# OUTPUT-
# Name of Student is Vanya Tripathi,Section is A, Course is SKG, and Roll number is 1
# Name of Student is Kartikey Dubey,Section is A, Course is B.Tech, and Roll number is 15


# Class related to __init__(constructor)

class Student2:

    def __init__(self, sname, scourse, ssection, srollno):
        self.name = sname
        self.Course = scourse
        self.Section = ssection
        self.Roll_no = srollno


Kartikey = Student2("Kartikey","B.Tech","A",15)

print("After calling __init__ Constructor")
print(Kartikey.name)
print(Kartikey.Course)
print(Kartikey.Section)
print(Kartikey.Roll_no)

#OUTPUT-
# After calling __init__ Constructor
# Kartikey
# B.Tech
# A
# 15