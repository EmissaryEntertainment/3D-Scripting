#THREE IS A CROWD
print("-------THREE IS A CROWD-------")
names = ["Jose", "Jim","Larry","Bran"]
def check_list(list):
    if len(list) > 3:
        print("This list is to crowded.")
check_list(names)
del names[0]
check_list(names)

#THREE IS A CROWD - PART 2
print("-------THREE IS A CROWD - PART 2-------")
def check_list_pt2(list):
    if len(list) > 3:
        print("This list is to crowded.")
    else:
        print("This list is a great size.")
check_list_pt2(names)

#SIX IS A MOB
print("-------SIX IS A MOB-------")
names.append("Steve")
names.append("Quincy")
def six_is_a_mob(list):
    if len(list) > 5:
        print("There is a mob in the room.")
    elif len(list) >= 3 and len(list) <= 5:
        print("This room is crowded.")
    elif len(list) == 1 or len(list) == 2:
        print("This room is not crowded.")
    else:
        print("The room is empty.")
six_is_a_mob(names)
