# Write a program that takes two integers, computes their sum, difference,
# product,and division,checks if they’re even/odd, and converts one to a float.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)

if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")

print("Float value of a:", float(a))