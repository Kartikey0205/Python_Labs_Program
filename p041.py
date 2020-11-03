# WAP of recursive function to display fibonaaci series upto N terms

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


num = int(input("Enter a number : "))
print("Fibonacci Series upto  ", num, " terms is : ")
for i in range(num + 1):
    print(fib(i), end=" ")
"""
OUTPUT:
Enter a number : 10
Fibonacci Series upto   10  terms is : 
0 1 1 2 3 5 8 13 21 34 55 
"""
