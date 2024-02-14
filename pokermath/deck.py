'''
deck class represents a 52 card deck
'''
from .card import Card
import random

class Deck:
    def __init__(self):
        # initialize a 52 card deck
        ranks = ["2", "3", "4", "5", "6", "7", 
                 "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards =  [Card(rank, suit) for suit in suits for rank in ranks]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        if (len(self.cards) == 0):
            return None
        
        return self.cards.pop()