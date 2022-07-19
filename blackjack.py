import random

class Card:
    def __init__ (self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.value = random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
        self.suit = suits[random.randrange(4)]

class Deck:
    def __init__(self):
        self.list_of_cards = ["Hearts", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], ["Diamonds", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], ["Spades", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], ["Clubs", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]    

    def draw_card_closed(self):
        c = Card()
        for i in range(4):
            if self.list_of_cards[i][0] == c.suit:
                if c.value in self.list_of_cards[i]:
                    #print(c.suit, c.value)
                    self.list_of_cards[i][self.list_of_cards[i].index(c.value)] = 0
                    break
                else:
                    self.draw_card_closed()            
        return(self)

    def draw_card_open(self, hand_or_table: list):
        c = Card()
        for i in range(4):
            if self.list_of_cards[i][0] == c.suit:
                if c.value in self.list_of_cards[i]:
                    hand_or_table.append(c.value + ' of ' + c.suit)
                    self.list_of_cards[i][self.list_of_cards[i].index(c.value)] = 0
                    break
                else:
                    self.draw_card_open(hand_or_table)            
        return(self)

def give_cards(self, hand: list):
    print("Ваши карты")
    [self.draw_card_open(hand) for i in range(2)]
    print(', '.join(hand))

def flop(self, table: list):
    print("Flop: ")
    self.draw_card_closed()
    [self.draw_card_open(table) for i in range(3)]
    print(', '.join(table))        

def turn(self, table: list):
    print("Turn:")
    self.draw_card_closed()
    self.draw_card_open(table)
    print(' '.join(table)) 

def river(self, table: list):
    print("River:")
    self.draw_card_closed()
    self.draw_card_open(table)
    print(', '.join(table)) 

d = Deck()
h1, h2,  f, t, r = [], [], [], [], []
counter = 0
give_cards(d, h1)
give_cards(d, h2)
flop(d, f)
turn(d, t)
river(d, r)
table = f + t + r
print(table)
