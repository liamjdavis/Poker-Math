'''
Player class represents a single player
'''
from .card import Card

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.hand = []
        self.current_bet = 0
    
    # actions
    def receive_card(self, card):
        self.hand.append(card)
    
    def fold(self):
        self.hand = []

    def bet(self, amount):
        if amount > self.money:
            raise ValueError("Bet cannot exceed current money")
        
        self.current_bet += amount
        self.money -= amount
    
    def win_pot(self, amount):
        self.money += amount