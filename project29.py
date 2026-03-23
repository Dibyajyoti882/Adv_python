#Create a function that takes base and exponent as input and returns base^exponent using loops (not using pow()).
def power(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

print(power(2,3))