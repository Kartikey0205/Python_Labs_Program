#WAP to explain concepts of global , scope , local variable

x=99
print("Original Global Variable ",x)
def fun():
    x = 20  #local variable

    def fun1():

        global x # make it global
        x = 88

        print("Value of fun()1'x is ", x)

    print('Before calling fun1() x is  ', x)

    fun1()  # call of fun1()
    print("After calling fun1() value of x is ", x)


fun()
print(x)
"""
OUTPUT:
Original Global Variable  99
Before calling fun1() x is   20
Value of fun()1'x is  88
After calling fun1() value of x is  20
88
"""

