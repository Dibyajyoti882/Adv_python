#1-Write a function to reverse a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
#2-Writw a function to check if a string is a palindrome.
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))
#3 Write a recursive function to find the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
#4 Write a function to count vowels in a string.
def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels("education"))
#5 Write a function to find the largest number in a list.
def largest_number(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

print(largest_number([10, 25, 5, 40, 15]))
#6 Write a function to check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
#7 Write a function to calculate the sum of digits of a number.
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print(sum_of_digits(1234))
#8 Write a function to generate First n fibonacci numbers.
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

fibonacci(7)
#9 Write a function to remove duplicates from a list while Keeping order
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print(remove_duplicates([1,2,2,3,4,4,5]))
#10 Write a function to find length of a string without using built-in len().
def string_length(s):
    count = 0
    for ch in s:
        count += 1
    return count

print(string_length("python"))