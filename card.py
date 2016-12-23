
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def IsAce(self):
        return self.rank == 'A'
