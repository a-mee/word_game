from word_game_functions import *
import time

def playGame(wordList):
    x = ''
    while x != 'e':
        x = input(
            'Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if x == 'r':
            try:
                playHand(hand, wordList, n)
            except NameError:
                print('You have not played a hand yet. Please play a new hand first!')
                print(' ')
        elif x == 'n':
            n = HAND_SIZE
            hand = dealHand(n)
            playHand(hand, wordList, n)
        elif x == 'e':
            break
        else:
            print('Invalid command.')


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
