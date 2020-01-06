import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()

    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print( card.show())

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self, num=1):
        length = len(self.cards)
        for _ in range(num):
            # This is the fisher yates shuffle algorithm
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
            # You can also use the built in shuffle method
            # random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        print( "Hi! My name is {}".format(self.name))
        return self

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self

    # Discards last card in player's hand
    def discardLast(self):
        return self.hand.pop()

    def discardCard(self, cardNum):
        indexCard = cardNum - 1
        del self.hand[indexCard]
# Test making a Card
# card = Card('Spades', 6)
# print card

# Test making a Deck
myDeck = Deck()
myDeck.shuffle()
# deck.show()

# Test making a player
dealer = Player("dealer")
dealer.sayHello()
dealer.draw(myDeck, 2)
dealer.showHand()
print("\n")

player1 = Player("Player1")
player1.sayHello()
player1.draw(myDeck, 2)
player1.showHand()
print("\n")

"""
player2 = Player("Player2")
player2.sayHello()
player2.draw(myDeck, 2)
player2.showHand()
print("\n")


player3 = Player("Player3")
player3.sayHello()
player3.draw(myDeck, 2)
player3.showHand()
print("\n")


player4 = Player("Player4")
player4.sayHello()
player4.draw(myDeck, 2)
player4.showHand()
print("\n")
"""
