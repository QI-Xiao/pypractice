# -*- coding: UTF-8 -*-
import random
import time
numb = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['C', 'D', 'H', 'S']


def generatecards():
    pock = []
    for i in numb:
        for j in suit:
            pock.append((i+j))
    pock.append('redlord')
    pock.append('blacklord')

    return pock


def dispatchcards(pock):
    random.shuffle(pock)
    lasted = pock[-3:]
    pock = pock[:-3]
    p1 = pock[::3]
    p2 = pock[1::3]
    p3 = pock[2::3]

    # random.shuffle(pock)
    # lasted = pock[-3:]
    # pock = pock[:-3]
    # p1 = []
    # p2 = []
    # p3 = []
    # while len(pock) > 0:
    #     p1.append(pock.pop())
    #     p2.append(pock.pop())
    #     p3.append(pock.pop())

    print(lasted)
    print(p1)
    print(p2)
    print(p3)


if __name__ == '__main__':
    cardPairs = generatecards()
    dispatchcards(cardPairs)
