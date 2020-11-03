# Write a function that accepts a string and calculates number of uppercase and lowercase letters.
def count(s):
    u, l = 0, 0
    for i in range(len(s)):
        if s[i] >= "A" and s[i] <= "Z":
            u += 1
        elif s[i] >= "a" and s[i] <= "z":
            l += 1
    return u, l


s = input("Enter a string:")
upper, lower = count(s)
print("\nUppercase characters:", upper)
print("Lowercase characters:", lower)

"""
OUTPUT:
Enter a string:Python Class

Uppercase characters: 2
Lowercase characters: 9

"""