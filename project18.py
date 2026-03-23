#Filter numeric values from a mixed-type tuple, attempt modification (handle error), and concatenate two tuples.
t = (1, "hi", 5, 9.5, 10)

nums = []
for i in t:
    if type(i) == int or type(i) == float:
        nums.append(i)

print("Numbers:", nums)

try:
    t[0] = 100
except:
    print("Tuple cannot be modified")

t2 = (100, 200)
print("Concatenated:", t + t2)