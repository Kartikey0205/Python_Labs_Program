# Display Fibonacci series up to 10 terms using loop.

fib = 0
a = -1
b = 1
c = 0
print("Fibonacci series upto 10 terms is : ")
for terms in range(0, 10):
    c = a + b

    print(c, end=" ")
    a = b
    b = c
"""
OUTPUT:
Fibonacci series upto 10 terms is : 
0 1 1 2 3 5 8 13 21 34 
"""