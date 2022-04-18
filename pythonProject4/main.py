from random import shuffle


class Card:
    suits = ["піка","чірва","бубна","хреста"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10",
             "валет", "дама", "король", "туз"]

    def __init__(self, v, s):
        self.suit = s
        self.value = v

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + "of" + self.suits[self.suit]
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player():
    def __int__(self, name1, name2):
        self.wins = 0
        self.card = None
        self.name1 = name1
        self.name2 = name2


class Game():
    def __init__(self):
        name1 = input("Вкажіть ім'я першого гравця:  ")
        name2 = input("Вкажіть ім'я другого гравця:  ")
        self.deck = Deck()
        self.p1 = name1
        self.p2 = name2

    def wins(self, winner):
        w = "{} заберає карти"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} кладе {}, а {} кладе {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Погнали")
        while len(cards) >= 2:
            m = ("""Натисніть клавішу "Х" для завершення гри,
            "або будь-яку іншу клавішу для продовження""")
            responce = input(m)
            if responce == "X":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1
            p2n = self.p2
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1)
            else:
                self.p2.wins += 1
                self.wins(self.p2)

        win = self.winner(self.p1, self.p2)

        print("Гра закінчена. {} виграв!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Нічия!"


game = Game()
game.play_game()





