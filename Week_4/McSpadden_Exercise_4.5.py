#GAME PREFERENCES
games = ["Anthem", "God Of War","Gears Of War", "Rainbow Six: Siege"]
for game in games:
    print("%s, is a game I enjoy." % game)
new_game = input("Enter a game you enjoy playing: ")
games.append(new_game)
for game in games:
    print("%s is a game we enjoy" % game)
