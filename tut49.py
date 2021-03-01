#Decorator in Python
def dec1(func1):
    def nowExecute():
        print("Executing dec1 function")
        func1()
        print("Executed")
    return nowExecute

@dec1
def hello():
    print("Hello from Kartikey")

# hello=dec1(hello)   --->> another way to show decorator is dec1()
hello()

# Output:
# Executing dec1 function
# Hello from Kartikey
# Executed
