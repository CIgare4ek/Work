my_words = ["слон", "апельсин", "банан", "яблуко"]


def hungman(word):
    wrong = 0
    stages = ["",
              "_____________             ",
              "|            |            ",
              "|            |            ",
              "|            O            ",
              "|          / | \          ",
              "|           / \           ",
              "|                         "
               ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    #print("Доброго вечора, ми з України! Тебе будуть казнити")
    while wrong < len(stages) - 1:
        print("\n")
        msg = input("Введіть букву: ")
        if msg in rletters:
            cind = rletters.index(msg)
            board[cind] = msg
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("Ти Українець і переміг! Було загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("Доброго вечора, ми з України! Тебе будуть казнити!\nБуло загадано слово: {}.".format(word))


my_words = ["Нікіта", "син", "слива", "сова", "язик", "мова", "школа"]

for word in my_words:
    hungman(word)