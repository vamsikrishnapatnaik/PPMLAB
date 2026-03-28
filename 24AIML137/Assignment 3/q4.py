# WAP to check whether the string is symmetrical or palindrome.

x = input("enter a string: ")
z = (str(str(x)[::-1]))

if x == z:
    print("it is a palindrome")
else:
    print("it is not a palindrome")