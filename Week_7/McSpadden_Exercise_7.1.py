import os
#PET NAMES
pet_dictionary = {"Liya": "Dog", "Midnight": "Cat", "Iggy": "Lizard"}

for key, value in pet_dictionary.items():
    print("%s is a %s" % (key, value))

#POLLING FREINDS
question_dictionary = {"Terry":" ","Jim":" ","Johnny":" "}
for name in question_dictionary:
    question_dictionary[name] = input("%s what is your favorite color? " % name)


for name, answer in question_dictionary.items():
    print("%s's favorite color is %s " % (name, answer))
os.system("pause")
