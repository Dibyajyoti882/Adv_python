#Find common elements between two lists using sets
a = {1,2,3,4,}
b= {3,4,5,6,}
print(a & b) 

#Remove duplicates from a sentence using sets
Sentence = "Good morning everyone"
words = set(Sentence.split())
print(words)
 
#check if two strings are anagrams using set and logic.
str1 = "listen"
str2 = "silent"
if set(str1) == set(str2) and len(str1) == len(str2):
    print("Anagrams")
else:
    print("Not Anagrams")



#find elements present in first list but not in second list using sets
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
set1 = set(list1)
set2 = set(list2)
difference = set1 - set2
print(difference)

#check if all characters in a string are unique using sets
string = "hello"
char_set = set()
for char in string:
    if char in char_set:
        print("Not all characters are unique.")
        break
    char_set.add(char)
else:    print("All characters are unique.")

#count numbers of distinct elements in a list using sets
numbers = [1,2,3,4,5,1,2,3]
distinct_numbers = set(numbers)
print(len(distinct_numbers))

#Find symmmetric difference between two sets without built in method
setA = {1,2,3,4}
setB = {3,4,5,6}
sym_diff = (setA - setB) | (setB - setA)
print(sym_diff)

#Remove common characters from two strings using sets
str1 = "abcdef"
str2 = "cdefgh"
set1 = set(str1)
set2 = set(str2)
unique_chars = (set1 - set2) | (set2 - set1)
print(''.join(unique_chars))

#Check if one set is a subset of another without built -in functions
setX = {1,2}
setY = {1,2,3,4,5}
is_subset = True
for item in setX:
    if item not in setY:
        is_subset = False
        break
print(is_subset)




#find repeated elements in a list using sets
numbers = [1,2,3,4,5]
repeated = set()
for num in numbers:
    if num in repeated:
        print(num)
    else:
        repeated.add(num)