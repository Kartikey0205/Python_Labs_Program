# WAP to enter a decimal number and display its binary , hex, octa equivalents and also its Square root.


n = int(input("Enter a decimal number "))
b = bin(n)
h = hex(n)
o = oct(n)
s = n ** (0.5)
print("The ", n, " in binary is ", b)
print("The ", n, " in hexa is ", h)
print("The ", n, " in octa is ", o)
print("The squareroot of ", n, "  is ", s)

"""
OUTPUT
Enter a decimal number 4
The  4  in binary is  0b100
The  4  in hexa is  0x4
The  4  in octa is  0o4
The squareroot of  4   is  2.0



"""
