# WAP to show the use of enumerate function

li = ["Capsicum", "Tomato", "Chopsticks", "Maggie"]
#  way to select odd-even pair via enumerate function

# here index will start from 0
for index, item in enumerate(li):
    if index % 2 == 0:
        print(f"Kartikey please buy {item}")


# Normal way to select odd-even pair is
i = 1
for item in li:
    if i % 2!= 0:
        print(f"Kartikey please buy {item}")
    i += 1

"""
OUTPUT:
Kartikey please buy Capsicum
Kartikey please buy Chopsticks
"""
