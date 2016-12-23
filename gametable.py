
from gamer import Gamer
from dealer import Dealer
from player import Player
from carddeck import CardDeck

class GameTable:
    def __init__(self, num_players, chips):
        self.dealer = Dealer()
        self.players = [None] * num_players
        self.num_players = num_players
        self.deck = CardDeck()
        
        for i in range(self.num_players):
            self.players[i] = Player(i, chips)
    
    def LeavePlayer(self, p):
        print('Player {} leaves the table...'.format(p.id))
        self.players[p.id] = None
        self.num_players -= 1
