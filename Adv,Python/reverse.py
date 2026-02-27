n = input("Enter a string: ")
reversed_n = n[::-1]
print("Reversed string:", reversed_n)

s = input("Enter a string: ")
upper = 0
lower = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
print("Uppercase:", upper)
print("Lowercase:", lower)


S = input("Enter a string: ")
count = 0
for i in S:
    if i.isdigit():
        count += 1
print("Number of digits:", count)

s = input("Enter string: ")
print(s.replace(" ", "_"))

s = input("Enter string: ")
freq = {}

for c in s:
    freq[c] = freq.get(c, 0) + 1

print(freq)

s = input("Enter string: ")
ch = input("Enter character: ")

print("First:", s.index(ch))
print("Last:", s.rindex(ch))

s = input("Enter string: ")
vowels = "aeiouAEIOU"
res = ""

for c in s:
    if c not in vowels:
        res += c

print(res)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")


s = input("Enter string: ")
print(s.title())


s = input("Enter string: ")
flag = True

for i in range(len(s)//2):
    if s[i] != s[len(s)-1-i]:
        flag = False
        break

print("Palindrome" if flag else "Not Palindrome")
