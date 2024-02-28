'''
Card class represents a single card
'''

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_values = {
            'Ace':14,
            'King':13,
            'Queen':12,
            'Jack':11,
        }

        for i in range(2, 11):
            self.rank_values[str(i)] = i

        for i in range(2, 11):
            self.rank_values[str(i)] = i
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"