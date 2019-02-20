def sports_team(city,team):
    print("The %s are a sports team in %s." % (team,city))

def world_languages(country,language):
    print("In %s they speak %s." % (country, language))

#SPORTS TEAMS
print("\n--------------- SPORTS TEAMS ---------------")
sports_team("San Diego", "Fleet")
sports_team("Philadelphia", "Eagles")
sports_team("San Diego","Gulls")

#WORLD LANGUAGES
print("\n--------------- WORLD LANGUAGES ---------------")
world_languages("The Unites States", "English")
world_languages("Mexico","Spanish")
world_languages("France","French")
