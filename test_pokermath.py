import pokermath as pm
import random

# set game constants
playerMoney = random.randint(500, 1000)
blinds = random.randint(0, 100)

# set players
players = []

names = ["Emily", "Jacob", "Sophia", "Michael", "Olivia", "William",
          "Ava", "Ethan", "Isabella", "James", "Mia", "Alexander", "Charlotte", 
          "Benjamin", "Amelia", "Mason", "Harper", "Elijah", "Evelyn", "Daniel"]

num_players = random.randint(1, len(names))

for i in range(num_players):
    players.append(pm.Player(name=names[i], money=playerMoney))

game = pm.Game(players=players, blinds=blinds)

# play a bunch of round
for i in range(100):
    winner = game.play_round()
    print(winner.name)