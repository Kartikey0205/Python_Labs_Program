# WAP to show various types of functions in Python
# 1) Default Argument
print("Default Length Argument")


def func(str_z, int_x, int_float):
    print(str_z)
    print(int_x)
    print(int_float)


func(int_float=627.89, int_x=98, str_z="hello")

# 2) Variable Length Argument
print("Variable Length Argument")


def fun(*favsub):
    for sub in favsub:
        print(sub)


fun("C-Langauge", "C++", "Python", "Web development")

"""
Output:
Default Length Argument
hello
98
627.89
Variable Length Argument
C-Langauge
C++
Python
Web development
"""