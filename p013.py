# WAP to write a Recursive function of Factorial


def recurs(n):
    if n == 1:
        return 1
    else:
        return n * recurs(n - 1)


number = int(input("Enter the number  "))

print("Factorial of ", number, " with recursive "
                               "approach is ", recurs(number))
"""

OUTPUT:
Enter the number  5
Factorial of  5  with recursive approach is  120
"""
