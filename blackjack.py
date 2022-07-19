import random

class Card:
    def __init__ (self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.value = random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
        self.suit = suits[random.randrange(4)]

class Deck:
    def __init__(self):
        self.list_of_cards = ["Hearts", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], \
        ["Diamonds", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], \
        ["Spades", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"], \
        ["Clubs", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]    

    def draw_card_closed(self, hand_or_table: list):
        c = Card()
        for i in range(4):
            if self.list_of_cards[i][0] == c.suit:
                if c.value in self.list_of_cards[i]:
                    self.list_of_cards[i][self.list_of_cards[i].index(c.value)] = 0
                    hand_or_table.append(c.value)
                    break
                else:
                    self.draw_card_closed(hand_or_table)            
        return(self)

    def draw_card_open(self, hand_or_table: list):
        c = Card()
        for i in range(4):
            if self.list_of_cards[i][0] == c.suit:
                if c.value in self.list_of_cards[i]:
                    hand_or_table.append(c.value)
                    self.list_of_cards[i][self.list_of_cards[i].index(c.value)] = 0
                    break
                else:
                    self.draw_card_open(hand_or_table)            
        return(self)

def sum_of_cards(hand_or_dealer: list):
    value = 0
    if "A" in hand_or_dealer:
        hand_or_dealer.remove("A")
        hand_or_dealer.append("A")
    for i in range(len(hand_or_dealer)):
        if hand_or_dealer[i] in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            value += int(hand_or_dealer[i])
        elif hand_or_dealer[i] == "A":
            if value > 10:
                value += 1
            else:
                value += 11
        else:
            value += 10
    return value


def give_cards(self, hand: list, dealer: list):
    [self.draw_card_open(hand) for i in range(2)]
    print("Ваши карты: ", ', '.join(hand))
    self.draw_card_open(dealer)
    print("Карты дилера: ", ''.join(dealer))
    self.draw_card_closed(dealer)

def hit(self, hand, name):
    self.draw_card_open(hand)
    print(name, ', '.join(hand))

money = 1000
quest = input("Добро пожаловать в казино 'Гнездо'. На вашем балансе 1000 яиц. Хотите сыграть? (y/n) ")
while quest == "y":
    d = Deck()
    h, dealer = [], []
    bet = int(input("Делайте ваши ставки! "))
    give_cards(d, h, dealer)
    answer = input("Ваши действия? (h/s) ")
    while answer == "h":
        hit(d, h, "Ваши карты")
        if sum_of_cards(h) > 21:
            break
        answer = input("Ваши действия? (h/s) ")
    while sum_of_cards(dealer) < 16:
        hit(d, dealer, "Карты дилера")
    print("Ваш счет: ", sum_of_cards(h), '\n', "Счет дилера: ", sum_of_cards(dealer))
    if (sum_of_cards(h) < 22 and sum_of_cards(h) > sum_of_cards(dealer)) or (sum_of_cards(h) < 22 and sum_of_cards(dealer) > 21):
        print("Вы победили!")
        money += bet
    else:
        print("Удачи в следующий раз!")
        money -= bet
    print("Ваш баланс: ", money)
    quest = input("Хотите сыгать еще? (y/n) ")
print("Спасибо за игру!")