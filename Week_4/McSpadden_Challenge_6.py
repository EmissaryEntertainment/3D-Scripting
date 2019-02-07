# Challenge 6 - Alien points
aliens = ["red","green","blue","red","green","blue","red","green","blue","green"]
score = 0

for alien in aliens:
    if alien == "red":
        score += 5
    elif alien == "green":
        score += 10
    elif alien == "blue":
        score += 20

print("If you destroy all aliens you will have %d points." % score)
