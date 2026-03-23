#Sort strings by length, identify palindromes, and replace spaces with hyphens using list comprehension.
lst = ["madam", "hello world", "python", "level"]

sorted_list = sorted(lst, key=len)
print("Sorted:", sorted_list)

pal = [x for x in lst if x == x[::-1]]
print("Palindromes:", pal)

new = [x.replace(" ", "-") for x in lst]
print("Spaces replaced:", new)