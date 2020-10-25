# WAP of args and kwargs

har = ["Kartikey", "Webdeveloper", "Rohan", "Android Developer",
       "Hacker", "shivam"]
nor = "Hello"


def funkwargs(norm, *args, **kwargs):
    print(norm)
    for items in args:
        print(items)
    for key, value in kwargs.items():
        print(key, value)

    print(f"{key} is a {value}")


har = ["Kartikey", "Webdeveloper", "Rohan", "Android Developer",
       "Hacker", "shivam"]
nor = "Hello"

kw = {"Kartikey": "programmer", "ALL_MY_SENIORS_JUNIORS_COLICS_FRIENDS_CLASSMATES_GF_ETC  "
: "Funny", "Kartikey Dubey": "Winner", "Rohan": "cook"}
funkwargs(nor, *har, **kw)
"""
Output:
Hello
Kartikey
Webdeveloper
Rohan
Android Developer
Hacker
shivam
Kartikey programmer
ALL_MY_SENIORS_JUNIORS_COLICS_FRIENDS_CLASSMATES_GF_ETC   Funny
Kartikey Dubey Winner
Rohan cook
Rohan is a cook
"""
