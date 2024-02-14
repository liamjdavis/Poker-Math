'''
Game class holds the game loop
'''
from .deck import Deck
from .player import Player
from .card import Card

class Game:
    def __init__(self, players, blinds):
        self.players = players
        self.blinds = blinds
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
    
    # game loop
    def play_round(self):
        # deal cards and collect blinds at start of round
        self.deal_cards()
        self.collect_blinds()

        # set loop flop, turn and river
        for i in range(5):
            self.add_communityCard

            # player logic
    
    # shuffle then deal cards
    def deal_cards(self):
        self.deck.shuffle()

        for player in self.players:
            # each player receives two cards
            player.receive_card(self.deck.deal_card)
            player.receive_card(self.deck.deal_card)
    
    # collect blinds
    def collect_blinds(self):
        for player in self.players:
            player.bet(self.blinds)
    
    # set flop
    def add_communityCard(self):
        self.community_cards.append(self.deck.deal_card)