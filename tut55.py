# WAP to demonstrate static Methods in Python.
class Student:

    @staticmethod
    def wish_User(string):
        print("Hello Good morning " + string)


Kartikey = Student()
Kartikey.wish_User("Kartikey")
#Output-
# Hello Good morning Kartikey