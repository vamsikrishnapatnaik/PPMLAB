# write a function to count vowels in a string.

def count_vowel(s):
    count = 0
    vowels = "aeiouAEIOU"
    for ch in s:
        if ch in vowels:
            count +=1
    return count

text = input("Enter a string : ")
print("Number of vowel :", count_vowel(text))