#Convert a mixed-type tuple to a list, remove integers less than 10, and convert back to a tuple.
t = (5, 15, 2, 20, 8)

lst = list(t)
lst = [x for x in lst if not(type(x) == int and x < 10)]

t = tuple(lst)
print("Final tuple:", t)