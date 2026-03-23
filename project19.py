#Create a student marks dictionary, then add, update, delete entries, and display keys, values, and items
d = {"A": 80, "B": 90}

d["C"] = 70
d["A"] = 85
del d["B"]

print("Keys:", d.keys())
print("Values:", d.values())
print("Items:", d.items())