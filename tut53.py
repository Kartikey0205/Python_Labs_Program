# WAP to demonstrate class Methods in Python.

class Student:
    no_of_leaves_granted = 8

    @classmethod # It changes something which is inside the class , here cls refer to class
    def change_leaves_granted(cls,new_leaves_granted):
        cls.no_of_leaves_granted=new_leaves_granted

Kartikey = Student()

Kartikey.change_leaves_granted(50)
print(Kartikey.no_of_leaves_granted)

# Output-
# 50
