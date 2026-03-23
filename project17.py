#Process a user-entered sentence: count vowels/consonants, reverse it, replace spaces with underscores, capitalize words.
s = input("Enter sentence: ")

vowels = "aeiouAEIOU"
v = c = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Reverse:", s[::-1])
print("Replace spaces:", s.replace(" ", "_"))
print("Capitalized:", s.title())