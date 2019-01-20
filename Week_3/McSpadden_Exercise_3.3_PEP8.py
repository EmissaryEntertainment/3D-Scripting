#WORKING LIST
careers = ["Programmer", "Sales Associate", "Technical Artist", "Teacher"]
print("The index of Sales Associate is: " + str(careers.index("Sales Associate")))
print("Technical Artist" in careers)
print("Baker" in careers)
careers.append("Baker")
careers.insert(0,"Janitor")
for index, career in enumerate(careers):
    print(str(index + 1)+": "+career)
#STARTING FROM EMPTY
newCareers = []
newCareers.append("Programmer")
newCareers.append("Sales Associate")
newCareers.append("Technical Artist")
newCareers.append("Teacher")
print("The first career in my new list is: " + newCareers[0])
print("The last career in my new list is: " + newCareers[3])
#ORDERED WORKING LIST
print("-------Here is the list in its original order-------")
for career in careers:
    print(career)
print("-------Here is the list in alphabetical order-------")
for career in sorted(careers):
    print(career)
print("-------Here is the list in its original order-------")
for career in careers:
    print(career)
print("-------Here is the list in reverse alphabetical order-------")
for career in sorted(careers, reverse = True):
    print(career)
print("-------Here is the list in its original order-------")
for career in careers:
    print(career)
print("-------Here is the list in reverse order-------")
careers.reverse()
for career in careers:
    print(career)
print("-------Here is the list in its original order-------")
careers.reverse()
for career in careers:
    print(career)
print("-------Here is the list in alphabetical order-------")
careers.sort()
for career in careers:
    print(career)
print("-------Here is the list in reverse alphabetical order-------")
careers.sort(reverse=True)
for career in careers:
    print(career)
#ORDERED NUMBERS
numbers = [5,3,1,2,4]
print("-------Here is the list in original order-------")
for number in numbers:
    print(number)
print("-------Here is the list in increasing order-------")
for number in sorted(numbers):
    print(number)
print("-------Here is the list in original order-------")
for number in numbers:
    print(number)
print("-------Here is the list in decreasing order-------")
for number in sorted(numbers,reverse = True):
    print(number)
print("-------Here is the list in original order-------")
for number in numbers:
    print(number)
print("-------Here is the list in reverse order-------")
numbers.reverse()
for number in numbers:
    print(number)
print("-------Here is the list in original order-------")
numbers.reverse()
for number in numbers:
    print(number)
print("-------Here is the list in increasing order-------")
numbers.sort()
for number in numbers:
    print(number)
print("-------Here is the list in decreasing order-------")
numbers.reverse()
for number in numbers:
    print(number)

listCount = len(careers)
print("The careers list has: " + str(listCount) + " elements in it")
listCount = len(newCareers)
print("The newCareers list has: " + str(listCount) + " elements in it")
listCount = len(numbers)
print("The numbers list has: " + str(listCount) + " elements in it")
