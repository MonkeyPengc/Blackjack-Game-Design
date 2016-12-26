# Blackjack Game Design in Python

Rules based on: http://www.bicyclecards.com/how-to-play/blackjack/

# How to Play

Please run client code (blackjack.py) through command line, and follow the instructions. 

# Design Concepts

### Main Entities(Sub Entities)

Gamer(Dealer, Player)

Card

CardDeck

GameTable

BlackjackManager

### Relation between Entities

A Dealer/Player is a Gamer.

A CardDeck has a specified amount of Cards.

A GameTable has one Dealer, Multiple Players and a CardDeck.

A BlackjackManager has a GameTable.

### Behaviors of Entities

BlackjackManager runs a GameTable, decides the winner in each single play, and terminates when there are no Players.

BlackjackManager shuffles the CardDeck when the system starts, or when there are less than 60 cards left.

GameTable joins or leaves Gamers.

The Dealer and multiple Players play a CardDeck with their own strategies.

The Dealer serves and deals with Players.

Players place bet, and make decisions in each single play.

Players choose to leave the GameTable, or forced to leave once below a certain amount of chips.






