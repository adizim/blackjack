import random
import time

CARD_VALUES = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

class Game:
    def __init__(self):
        self.deck = CARD_VALUES.keys()*4
        random.shuffle(self.deck)
        self.dealer_hand, self.player_hand = Hand("Dealer Hand", hidden=True), Hand("Player Hand", hidden=False)
        self.dealer_hand.cards.extend([self.deck.pop(), self.deck.pop()])
        self.player_hand.cards.extend([self.deck.pop(), self.deck.pop()])

    def player_loop(self):
        if self.player_hand.value() == 21:
            print("Blackjack! You win!")
            return True
        while input("Hit (1) or Hold (0): "):
            self.player_hand.hit(self.deck.pop())
            print(self.player_hand)
            if self.player_hand.value() > 21:
                print("Player Bust. You lose!")
                return True
        return False

    def dealer_loop(self):
        if self.dealer_hand.value() == 21:
            print("Blackjack! You lose!")
            return True
        while self.dealer_hand.value() < 17:
            time.sleep(1)
            self.dealer_hand.hit(self.deck.pop())
            print(self.dealer_hand)
            if self.dealer_hand.value() > 21:
                print("Dealer Bust. You win!")
                return True
        return False

    def __repr__(self):
        return "{}\n{}".format(self.dealer_hand, self.player_hand)

    def run(self):
        print(self)
        if self.player_loop():
            return
        self.dealer_hand.hidden = False
        print(self.dealer_hand)
        if self.dealer_hand.value() == 21:
            print("Blackjack! You lose!")
            return
        if self.dealer_loop():
            return
        print(self.player_hand) 
        if self.player_hand.value() > self.dealer_hand.value():
            print("You win!")
        elif self.player_hand.value() == self.dealer_hand.value():
            print("Tie game.")
        else:
            print("You lose!")            

class Hand:
    def __init__(self, name, hidden):
        self.name = name
        self.hidden = hidden
        self.cards = []

    def value(self):
        CARD_VALUES.update({"A":11})
        hard = sum([CARD_VALUES[card] for card in self.cards]) 
        CARD_VALUES.update({"A":1})
        soft = sum([CARD_VALUES[card] for card in self.cards]) 
        if hard <= 21:
            return hard
        else:
            return soft

    def hit(self, card):
        self.cards.append(card)

    def __repr__(self):
        if self.hidden:
            return "{}: {},? Value ?".format(self.name, self.cards[0], self.value())
        return "{}: {} Value {}".format(self.name, ",".join(self.cards), self.value())

if __name__ == "__main__":
    while input("Play Blackjack?\nYes (1) or No (0): "):
        Game().run()