#String Pattern Validator Input a string and check whether it’s a palindrome. Count total vowels, consonants, digits, and special characters using loops and conditions.
s = input("Enter string: ")

print("Palindrome:", s == s[::-1])

v = c = d = sp = 0

for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print(v, c, d, sp)