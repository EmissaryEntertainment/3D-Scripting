#MOUNTAIN HEIGHTS
mountain_dictionary = {"Mount Everest":"8,848","K2":"8,611","Broad Peak":"8,051","Coropuna":"6,425","Mount Logan":"5,959"}

print("MOUNTAIN RANGE NAMES")
for key in mountain_dictionary:
    print("Mountain name: %s" %key)

print("\nMOUNTAIN RANGE HEIGHTS")
for value in mountain_dictionary.values():
    print("Mountain height in meters: %s" %value)

print("\nMOUNTAIN RANGE NAMES AND HEIGHTS")
for key, value in mountain_dictionary.items():
    print("%s is %s meters tall." % (key,value))


#MOUNTAIN HEIGHTS 2 - Values printed in alphabetical order
print("\nMOUNTAIN RANGE NAMES AND HEIGHTS IN ALPHABETICAL ORDER")
for key, value in sorted(mountain_dictionary.items()):
    print("%s is %s meters tall." % (key,value))
