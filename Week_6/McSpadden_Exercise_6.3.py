import pickle
import os

def print_title_bar(_games):
    print("**********************************************")
    print("***  Games list - there are currently %d games in the list  ***" % len(_games) )
    print("**********************************************")

def load_games_list(_games):
    if len(_games) > 0:
        for game in _games:
            print("The following game was loaded from the file: %s" % game)
    else:
        print("There was no list of games to load.")

def add_game(_games):
    new_game = ""
    in_list = False
    new_game = input("Enter a new game to add to the list: ")
    for game in _games:
        if new_game == game:
            print("That game is already in your list.")
            in_list = True
    if in_list == False:
        _games.append(new_game)
    return _games

def quit():
    try:
        file_object = open("Exercise_6.3.pydata", "wb")
        pickle.dump(games, file_object)
        file_object.close()

        print("I will remember the following games: ")
        for game in games:
            print(game)
    except Exception as e:
        print(e)
        print("I couldn't figure out how to store the games, sorry.")
    os.system("pause")

def run_program(_games):
    choice = ""
    while choice != "3":
        print_title_bar(_games)
        choice = input("[1] See current list of games. \n[2] Add a game to your list. \n[3] Quit the application. ")
        if choice == "1":
            load_games_list(_games)
            os.system("pause")
            os.system("cls")
        elif choice == "2":
            games = add_game(_games)
            os.system("pause")
            os.system("cls")
        elif choice == "3":
            quit()
        else:
            print("Sorry, that is not an accepted input. Please try again.")
            os.system("pause")

try:
    file_object = open("Exercise_6.3.pydata", "rb")
    games = pickle.load(file_object)
    file_object.close()
except:
    games = []

run_program(games)
