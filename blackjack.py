
import sys

from gametable import GameTable
from carddeck import CardDeck



class BlackjackManager:
    def __init__(self, num_players=5, chips_for_players=500):
        self.game_table = GameTable(num_players, chips_for_players)
        self.game_status = False
    
    def RunGame(self):
        self.game_status = True
        self.game_table.deck.Shuffle()
        
        while self.game_status:
            if self.game_table.deck.CheckLess60():
                self.game_table.deck = CardDeck()
                self.game_table.deck.Shuffle()
            
            self.StartToServe()
            self.game_status = self.CheckTable()

        sys.exit(1)

    def CheckTable(self):
        return self.game_table.num_players >= 1
    
    def StartToServe(self):
        ## reset players
        self.Reset()
        
        ## show initial player status
        self.ShowPlayerStatus()
        
        self.AskToPlaceBet()
        
        ## show player status after bet
        self.ShowPlayerStatus()
        
        for i in range(2):
            self.game_table.dealer.WantCard(self.game_table.deck)
            
            for p in self.game_table.players:
                if not p:
                    continue
                
                p.WantCard(self.game_table.deck)
    
        self.ShowDealerHand(reveal=False)
        self.ShowPlayerHand()
        
        self.PlayersTurn()
        
        while not self.game_table.dealer.CheckBigger17():
            self.game_table.dealer.WantCard(self.game_table.deck)
        
        self.ShowDealerHand()
        
        self.DecideWinner()

        self.AskToPlayAgain()
    
    def ShowPlayerStatus(self):
        for p in self.game_table.players:
            if not p:
                continue
            
            print("Player {0} current chips: ${1} bet: ${2} ".format(p.id, p.chips, p.bet))

    def AskToPlaceBet(self):
        for p in self.game_table.players:
            if not p:
                continue

            while True:
                try:
                    bet = int(input("Player {0}, how much would you like to bet? $".format(p.id)))
                    
                except (SyntaxError, ValueError, NameError):
                    print("Oops! That was an invalid number. Try again...")
                
                else:
                    if bet > p.chips:
                        print("Your bet is over your chips.")
                        continue

                    if bet < 5 or bet > 500:
                        print("Your bet is out of limit(5-500).")
                        continue

                    break
    
            if bet:
                p.PlaceBet(self.game_table.dealer, bet)
                    
            else:
                sys.exit(1)

    def ShowPlayerHand(self):
        for p in self.game_table.players:
            if not p:
                continue
            
            print("Player {0} has cards {1}.".format(p.id, p.ShowHand()))

    def ShowDealerHand(self, reveal=True):
        if not reveal:
            print("Dealer has cards 'XX' and {}.".format(self.game_table.dealer.ShowHand(reveal=False)))
        
        else:
            print("Dealer has cards {}.".format(self.game_table.dealer.ShowHand()))

    def PlayersTurn(self):
        for p in self.game_table.players:
            if not p:
                continue
            
            print("Now serving Player {0}, Cards {1}...".format(p.id, p.ShowHand()))
            player_score = p.CalculateScore()
            
            ## if player goes bust, he loses the bet, even if the dealer goes bust as well
            if p.IsBust(player_score):
                self.game_table.dealer.Deal(p)
        
            ## if player stands at 21 or less, the dealer asks the player hit or stand
            else:
                hit = self.game_table.dealer.HitOrStand(p)
                
                while hit:
                    p.WantCard(self.game_table.deck)
                    player_score = p.CalculateScore()
                    print("Player {0}, Cards {1}.".format(p.id, p.ShowHand()))
                    if p.IsBust(player_score):
                        break
                
                    hit = self.game_table.dealer.HitOrStand(p)
                
                ## if the player goes bust, he loses the bet.
                if p.IsBust(player_score):
                    self.game_table.dealer.Deal(p)
                
                ## if the player stands at 21 or less, the dealer continues to serve the next player
                else:
                    print("Done! Player {0} stands at {1} score {2}.".format(p.id, p.ShowHand(), player_score))

    def DecideWinner(self):
        dealer_score = self.game_table.dealer.CalculateScore()
        dealer_bust = self.game_table.dealer.IsBust(dealer_score)
        
        ## pick active players
        players = [p for p in self.game_table.players if p and p.play_status]
        
        for p in players:
            player_score = p.CalculateScore()
            
            ## tie
            if dealer_score == player_score:
                self.game_table.dealer.Deal(p, tie=True)
            
            ## dealer wins
            elif not dealer_bust and dealer_score > player_score:
                self.game_table.dealer.Deal(p)
        
            ## player wins
                ## player wins by get a Natural
                ## player wins by a higher score or dealer busts
            else:
                if player_score == 21:
                    self.game_table.dealer.Deal(p, player_win=True, player_natural=True)
                
                else:
                    self.game_table.dealer.Deal(p, player_win=True)

    def AskToPlayAgain(self):
        for p in self.game_table.players:
            if not p:
                continue
        
            if p.chips < 5:
                self.game_table.LeavePlayer(p)
        
            else:
                while True:
                    try:
                        play = p.PlayAgain()

                    except (SyntaxError, ValueError, NameError):
                        print("Oops! That was an invalid answer. Try again...")

                    else:
                        break

                if not play:
                    self.game_table.LeavePlayer(p)


    def Reset(self):
        for p in self.game_table.players:
            if not p:
                continue
            
            p.hands = []
            p.bet = 0
            p.play_status = True
        
        self.game_table.dealer.hands = []




if __name__ == "__main__":


    print("*******************************************************")
    print("*             Blackjack - Welcome!                    *")
    print("*               2016 Cheng Peng                       *")
    print("*******************************************************")



    while True:
        try:
            num_players = int(input("Enter the number of players(1-5): "))
    
        except (SyntaxError, ValueError, NameError):
            print("Oops! That was an invalid answer. Try again...")

        else:
            if num_players >= 1 and num_players <= 5:
                break
            
            print("At least 1 player, and at most 5 players to start the game...")


    while True:
        try:
            chips_for_players = int(input("Enter an initial amount of chips for each player(>=$5): "))

        except:
            print("Oops! That was an invalid answer. Try again...")

        else:
            if chips_for_players >= 5:
                break

            print("Each player must have at least $5 to start the game...")


    app = BlackjackManager(num_players, chips_for_players)

    app.RunGame()








