#WAP to explain the use of Instance variable and Class Variable in Python.
class Student:
    no_of_leaves_granted=8
    pass


Kartikey = Student()
Vanya = Student()

# print(Kartikey, Vanya)
Kartikey.name = "Kartikey Dubey"
Kartikey.Section = "A"
Kartikey.Course = "B.Tech"
Kartikey.Roll_no = 15

Vanya.name = "Vanya Tripathi"
Vanya.Section = "A"
Vanya.Course = "SKG"
Vanya.Roll_no = 1
print(Kartikey.Roll_no, Kartikey.no_of_leaves_granted,"\n", Vanya.Roll_no,Vanya.no_of_leaves_granted)
Kartikey.no_of_leaves_granted =10
print(Kartikey.Roll_no, Kartikey.no_of_leaves_granted)

Student.no_of_leaves_granted=17
print(Student.no_of_leaves_granted)

#Output-
# 15 8
#  1 8
# 15 10
# 17
