import pickle
import os

try:
    file_object = open("games.pydata", "rb")
    games = pickle.load(file_object)
    file_object.close()
except:
    games = []

if len(games) > 0:
    for game in games:
        print("The following games were loaded from the file: %s" % game)
else:
    print("There was no list games to load.")

new_game = ""
while new_game != "quit":
    new_game = input("Enter a game you enjoy playing, or type 'quit' to exit: ")
    if new_game != "quit":
        games.append(new_game)

try:
    file_object = open("games.pydata", "wb")
    pickle.dump(games, file_object)
    file_object.close()

    print("I will remember the following games: ")
    for game in games:
        print(game)
except Exception as e:
    print(e)
    print("I couldn't figure out how to store the games, sorry.")
os.system("pause")
