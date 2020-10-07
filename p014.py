# WAP to write a Recursive function of Fibonnacci Series

def fibonaci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)


number = int(input("Enter the number upto which you want to see fibonaci series sum: "))
print("Fibonacci sum upto ", number, " with recursive "
                                 "approach is ", fibonaci(number))

"""
OUTPUT:
Enter the number upto which you want to see fibonaci series sum: 8
Fibonacci sum upto  8  with recursive approach is  13
"""