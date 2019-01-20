# First: is to store a quote and print it back out.
quote = "Steven Kings words of advice, 'Get busy living or get busy dying.'"
print(quote)

# Second: is to store your name in lowercase, then print it back in lowercase, Titlecase, and UPPERCASE.
first_name = "garrett"
print(first_name)
print(first_name.capitalize())
print(first_name.upper())

# Third: store first name and last name in separate variables then concatenate them together.
# first name is already stored above.
last_name = "mcspadden"
print(first_name.capitalize() + ' ' + last_name.capitalize())

# Fourth: Choose a person, store their first and last name in separate variables.
# then use concatenation to make a sentence stored in a third variable, then print the whole sentence.
# I will reuse my firstName and lastName variables from above.
first_name = "Roderick"
last_name = "McMillen"
sentence = first_name + " " + last_name + " is my grandfather, as well as an extraordinary man."
print(sentence)

# Fifth: Store your first name in a variable, include at least two kinds of whitespace on each side of your name.
# Print your name as it is stored.
# Print your name with whitespace stripped from the left side, then from the right side, then from both sides.
# Again i will use the same firstName variable from above.
first_name = "      Garrett      "
print(first_name +" - this is normal")
print(first_name.lstrip() +" - this is with left space stripped")
print(first_name.rstrip()+" - this is with right space stripped")
print(first_name.strip()+" - this is with all spaces stripped")
