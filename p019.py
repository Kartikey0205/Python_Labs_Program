#WAP of string, display only those characters which are present at an even index number. For example str = "computer" so you should display ‘c’, ‘m’, ‘u’, ‘e’.

string=input("Enter any word : ")
for i in range(len(string)):
    if(i%2==0):
        print("Even index number string letter are : ",string[i])

"""
OUTPUT:
Enter any word : computer
Even index number string letter are :  c
Even index number string letter are :  m
Even index number string letter are :  u
Even index number string letter are :  e

"""