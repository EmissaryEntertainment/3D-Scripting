#GREETER
names = ["Steve","Bob","Joe"]
def greet(name):
    print("Hello %s" % name)
    print("%s is your name." % name)
    print("How are you %s?" % name)
for name in names:
    greet(name)

#FULL NAMES
def full_names(first_name,last_name):
    print("Welcome to the Matrix, %s %s" % (first_name, last_name))
full_names("Steve","Wilkes")
full_names("Joe","Wilhelm")
full_names("Bob","LaRoe")

#ADDITION CALCULATOR
def addition(first_number,second_number):
    print("The sum of %s and %s is %s" % (first_number, second_number, first_number+second_number))
addition(1,5)
addition(10,2)
addition(5,9)

#RETURN CALCULATOR
def addition(first_number,second_number):
    return first_number+second_number
print("The sum of 5 and 6 is %s" % addition(5,6))
