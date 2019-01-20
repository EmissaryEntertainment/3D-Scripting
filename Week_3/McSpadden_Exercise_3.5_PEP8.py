# ALPHABET SLICE
alphabet = ["a","b","c","d","e","f","g","h","i","j"]
slice = alphabet[0:3]
for letter in slice:
    print("First slice: " + letter)
slice = alphabet[4:8]
for letter in slice:
    print("Second slice: " + letter)
slice = alphabet[2:]
for letter in slice:
    print("Third slice: " + letter)
# PROTECTED LIST
list = ["Jim", "Bob", "Joe"]
list_copy = list[:]
list_copy.insert(0,"Quincy")
for name in list:
    print("Original list names: " + name)
for name in list_copy:
    print("listCopy names: " + name)
