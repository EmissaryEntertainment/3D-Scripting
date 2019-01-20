#LISTING A SENTENCE
sentence = "This is the sentence I wrote."
for letter in sentence:
    print(letter)

#SENTENCE LIST
sentenceList = [letter for letter in sentence]
print(sentenceList)

#SENTENCE SLICES
print(sentence[:5])
print(sentence[12:17])
print(sentence[-5:])

#FINDING PYTHON
sentence = "Python is the language I am using to write this message about Python."
print("Python" in sentence)
print(sentence.find("Python"))
print(sentence.rfind("Python"))
print(sentence.count("Python"))
words = sentence.split(" ")
print(words)
for word in words:
    print(word)
sentence = sentence.replace("Python","Ruby")
print(sentence)
