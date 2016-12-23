
from card import Card
import random

class CardDeck:
    def __init__(self, num_deck=6):
        RANKS = '23456789TJQKA'
        SUITS = 'SHDC'
        
        self.cards = []
        self.totalCards = 0
        
        for i in range(num_deck):
            for rank in RANKS:
                for suit in SUITS:
                    self.cards.append(Card(rank, suit))
                    self.totalCards += 1

    def Shuffle(self):
        print("Shuffling the deck...")
        random.shuffle(self.cards)

    def PopCard(self):
        card = self.cards.pop()
        self.totalCards -= 1
        return card

    def CheckLess60(self):
        return self.totalCards <= 60
    
    def CheckEmpty(self):
        return self.totalCards == 0
