import string

s = input("")
cs = ''.join(char for char in s if char not in string.punctuation)
print(cs)