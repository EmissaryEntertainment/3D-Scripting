#MOUNTAIN HEIGHTS 3
original_mountain_dictionary = {"Mount Everest":8848,"K2":8611,"Broad Peak":8051,"Coropuna":6425,"Mount Logan":5959}
new_mountain_dictionary = {}

for key, value in original_mountain_dictionary.items():
    new_mountain_dictionary[key] = [str(value) , str(int(value*3.28))]

print("MOUNTAIN RANGE NAMES")
for key in new_mountain_dictionary:
    print("Mountain name: %s" % key)

print("\nMOUNTAIN RANGE HEIGHTS IN METERS")
for value in new_mountain_dictionary.values():
    print("Mountain height in meters: %s" % value[0])

print("\nMOUNTAIN RANGE HEIGHTS IN FEET")
for value in new_mountain_dictionary.values():
    print("Mountain height in feet: %s" % value[1])

print("\nMOUNTAIN RANGE NAMES AND HEIGHTS")
for key, value in new_mountain_dictionary.items():
    print("%s is %s meters tall, or %s feet." % (key,value[0],value[1]))

#MOUNTAIN HEIGHTS 4
mountain_dictionary = {"Mount Everest":{"Elevation":"8,848","Range":"Himalaya"},
                        "K2":{"Elevation":"8,611","Range":"Karakoram"},
                        "Broad Peak":{"Elevation":"8.051","Range":"Karakoram"},
                        "Coropuna":{"Elevation":"6,425","Range":"Andes, Peru"},
                        "Mount Logan":{"Elevation":"5,959","Range":"Saint Elias Mountain"}}

print("\n----------------- MOUNTAIN HEIGHT 4 ------------------")
print("\nMOUNTAIN NAMES")
for name in mountain_dictionary:
    print(name)

print("\nMOUNTAIN ELEVATIONS")
for elevation in mountain_dictionary.values():
    print(elevation["Elevation"])

print("\nMOUNTAIN RANGES")
for range in mountain_dictionary.values():
    print(range["Range"])

print("\nFULL MOUNTAIN INFORMATION")
for name, value in mountain_dictionary.items():
    print("%s is %s meters tall, and is in the %s range." % (name,value["Elevation"],value["Range"]))
