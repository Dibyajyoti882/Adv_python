#Unique Character Extractor Input a sentence and print characters that appear only once. Ignore spaces and punctuation. Use sets and loops to identify uniqueness
s = input("Enter string: ")

for ch in s:
    if s.count(ch) == 1 and ch.isalnum():
        print(ch, end=" ")