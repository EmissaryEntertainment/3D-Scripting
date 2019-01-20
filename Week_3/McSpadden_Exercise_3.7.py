#MULTIPLES OF TEN
tens = [number*10 for number in range(1,11)]
print(tens)

#CUBES
cubes = [number**3 for number in range(1,11)]
print(cubes)

#AWESOMENESS
names = ["Bob","Jim","Mel","Sam","Todd"]
awesomeNames = [name + " is awesome!" for name in names]
print(awesomeNames)

#WORKING BACKWARDS
plusThirteen = []
for number in range(1,11):
    newThirteen = number + 13
    plusThirteen.append(newThirteen)
print(plusThirteen)
