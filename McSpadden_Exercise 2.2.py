#First: is to store a quote and print it back out.
quote = "Steven Kings words of advice, 'Get busy living or get busy dying.'"
print(quote)

#Second: is to store your name in lowercase, then print it back in lowercase, Titlecase, and UPPERCASE.
firstName = "garrett"
print(firstName)
print(firstName.capitalize())
print(firstName.upper())

#Third: store first name and last name in separate variables then concatenate them together.
#first name is already stored above.
lastName = "mcspadden"
print(firstName.capitalize() + ' ' + lastName.capitalize())

#Fourth: Choose a person, store their first and last name in separate variables.
#then use concatenation to make a sentence stored in a third variable, then print the whole sentence.
#I will reuse my firstName and lastName variables from above.
firstName = "Roderick"
lastName = "McMillen"
sentence = firstName + " " + lastName + " is my grandfather, as well as an extraordinary man."
print(sentence)

#Fifth: Store your first name in a variable, include at least two kinds of whitespace on each side of your name.
#Print your name as it is stored.
#Print your name with whitespace stripped from the left side, then from the right side, then from both sides.
#Again i will use the same firstName variable from above.
firstName = "      Garrett      "
print(firstName +" - this is normal")
print(firstName.lstrip() +" - this is with left space stripped")
print(firstName.rstrip()+" - this is with right space stripped")
print(firstName.strip()+" - this is with all spaces stripped")