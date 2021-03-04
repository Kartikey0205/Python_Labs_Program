# Write a first class program in Python.
class Student:
    pass


Kartikey = Student()
Vanya = Student()

print(Kartikey, Vanya)
Kartikey.name = "Kartikey Dubey"
Kartikey.Section = "A"
Kartikey.Course = "B.Tech"
Kartikey.Roll_no = 15

Vanya.name = "Vanya Tripathi"
Vanya.Section = "A"
Vanya.Course = "SKG"
Vanya.Roll_no = 1

print(Kartikey.name,"\n", Vanya.name)
#Output-
# <__main__.Student object at 0x01C21FB8> <__main__.Student object at 0x01C21FE8>
# Kartikey Dubey
#  Vanya Tripathi
