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
        self.hand_rankings = self.set_handRankings()
    
    # game loop
    def play_round(self):
        # deal cards and collect blinds at start of round
        self.deal_cards()
        self.collect_blinds()

        # reset community cards
        self.community_cards = []

        # set loop flop, turn and river
        for i in range(5):
            self.add_communityCard

            # player logic
            for player in self.players:
                # default: all players bet blinds amount
                player.bet(self.blinds)
        
        winner = self.getWinner(self.players, self.community_cards)
    
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
    
    # determine winner
    def getWinner(players, community_cards):
        rankings = []
        winner = None

        # iterate through the players hands
        for player in players:
            hand = player.get_hand() + community_cards

            # classify hand
            hand_class = self.classify_hand(hand)
            rankings.append(self.hand_rankings[hand_class])

        return
    
    # set hand rankings
    def set_handRankings():
        rankings = {
            "High Card": 0,
            "One Pair": 1,
            "Two Pair": 2,
            "Three of a Kind": 3,
            "Straight": 4,
            "Flush": 5,
            "Full House": 6,
            "Four of a Kind": 7,
            "Straight Flush": 8,
            "Royal Flush": 9
        }

        return rankings

    # hand classifier
    def classify_hand(hand):
        # give new variable for sorted hand
        sorted_hand = sorted(hand for card in hand)

        # count occurrences of each suit
        suit_counts = {}

        for card in hand:
            if card.suit in suit_counts:
                suit_counts[card.suit] += 1
            else:
                suit_counts[card.suit] = 1
        
        num_suits = len(suit_counts)

        # for 1 suit in hand
        if num_suits == 1:
            # check for royal flush
            royal_flush = ["10", "Jack", "Queen", "King", "Ace"]

            if sorted_hand == royal_flush:
                return "Royal Flush"
            
            # check for straight flush
            elif sorted_hand == hand:
                return "Straight Flush"
            
            # else it's just a flush
            else:
                return "Flush"
        
        # count occurrences of rank
        rank_counts = {}

        for card in hand:
            if card.rank in rank_counts:
                rank_counts[card.rank] += 1
            else:
                rank_counts[card.rank] = 1
        
        num_ranks = len(rank_counts)
        values = list(rank_counts.values)

        # check for straight
        if num_suits >= 5 and num_ranks >= 5:
            return "Straight"

        # hands regardless of suit
        # check for four of a kind
        if values.count(4) == 1:
            return "Four of a Kind"
        
        # check for full house
        elif values.count(3) == 1 and values.count(2) == 1:
            return "Full House"
        
        # check for 3 of a kind
        elif values.count(3) == 1:
            return "Three of a Kind"
        
        # check for two pair
        elif values.count(2) == 2:
            return "Two Pair"
        
        # check for one pair
        elif values.count(2) == 1:
            return "One Pair"
        
        # return high card
        else:
            return "High Card"
            
