# Create a game dictionary
games = {
}

# Get user input
game_count = int(input("How many games do you want to add?: "))

#For Loops

for i in range(game_count):
    game_name = input("Enter the name of a game: ")
    game_description = input("Enter a description for the game you have entered: ")
    # Adding the to dictionary.
    games[game_name] = game_description


#Print game dictionary
print(games)

