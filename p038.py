# Write a function func1() such that it can accept a variable length
# of arguments and print all argument values

def func1(name, *favSub):
    print(name)
    for sub in favSub:
        print(sub, end=" ")


func1("Deepika", "maths", "python", "data structure", "Ruby")

"""
OUTPUT:
Deepika
maths python data structure Ruby 
"""
