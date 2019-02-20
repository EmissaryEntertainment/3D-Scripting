#FUNCTIONS
def print_animals_dictionary(dictionary):
    for key, value in dictionary.items():
        print("%s is a %s." % (key, value))

def print_weightlift_dictionary(dictionary):
    for key, value in dictionary.items():
        print("For %s you should do %s reps." % (key, value))

#PET NAMES 2
pet_dictionary = {"Liya": "Dog", "Midnight": "Cat", "Iggy": "Lizard"}
print_animals_dictionary(pet_dictionary)

pet_dictionary["Liya"] = "Hamster"
print_animals_dictionary(pet_dictionary)

pet_dictionary["Spot"] = "Doggo"
print_animals_dictionary(pet_dictionary)

del pet_dictionary["Midnight"]
print_animals_dictionary(pet_dictionary)

#WEIGHT LIFTING
weightlift_dictionary = {"Bench Press":"10","Squats":"15","Crunches":"12"}
print_weightlift_dictionary(weightlift_dictionary)

weightlift_dictionary["Crunches"] = "20"
print_weightlift_dictionary(weightlift_dictionary)

weightlift_dictionary["Lunges"] = "15"
print_weightlift_dictionary(weightlift_dictionary)

del weightlift_dictionary["Bench Press"]
print_weightlift_dictionary(weightlift_dictionary)
