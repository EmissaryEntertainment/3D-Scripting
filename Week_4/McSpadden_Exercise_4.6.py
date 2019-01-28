#MANY GAMES
games = ["Anthem", "God Of War","Gears Of War", "Rainbow Six: Siege"]
for game in games:
    print("%s, is a game I enjoy." % game)
new_game = ""
while new_game != 'quit':
    new_game = input("Enter a game you enjoy playing, or type 'quit' to exit: ")
    games.append(new_game)
for game in games:
    print("%s is a game we enjoy" % game)
