# DESCRIPTION:
# The objective of Duck, duck, goose is to walk in a
#  circle, tapping on each player's head until one is
#   chosen.

# Task: Given an array of Player objects
#  (an array of associative arrays in PHP) and an index
#   (1-based), return the name of the chosen
#    Player(name is a property of Player objects,
#     e.g Player.name)

#solution
def duck_duck_goose(players, goose):
    length = len(players)
    if goose <= length:
        return players[goose - 1].name
    else:
        return players[(goose % length) - 1].name

