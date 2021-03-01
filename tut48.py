#Map , Filter , Reduce in Python

# --------------------------MAP------------------------------


def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]

for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

# --------------------------FILTER------------------------------
list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)
# --------------------------REDUCE------------------------------
from functools import reduce

list1 = [1, 2, 3, 4, 2]
num = reduce(lambda x, y: x * y, list1)

print(num)

# OUTPUT:
# [0, 0]
# [1, 1]
# [4, 8]
# [9, 27]
# [16, 64]
# [6, 7, 8, 9]
# 48