# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"


def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def getWordScore(word, n):
    wScore = 0
    for letter in word:
        wScore += SCRABBLE_LETTER_VALUES[letter]
    wScore = wScore * len(word)
    if len(word) == n:
        wScore += 50
    return wScore


def displayHand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line


def dealHand(n):
    hand = {}
    numVowels = n // 3

    for i in range(numVowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(numVowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


def updateHand(hand, word):
    nHand = hand.copy()
    for letter in word:
        nHand[letter] -= 1
    return nHand


def isValidWord(word, hand, wordList):
    if word in wordList:
        dicWord = getFrequencyDict(word)
        for letter in dicWord.keys():
            if letter not in hand or dicWord[letter] > hand[letter]:
                return False
        return True
    else:
        return False


def calculateHandlen(hand):
    return sum(hand.values())


def playHand(hand, wordList, n):
    # Keep track of the total score
    totalScore = 0
    nHand = hand.copy()
    newN = n
    # As long as there are still letters left in the hand:
    while newN > 0:
        # Display the hand
        print('Current Hand: ', end='')
        displayHand(nHand)
    # Ask user for input
        word = input(
            'Enter word, or a "." to indicate that you are finished: ')
    # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break
    # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, nHand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print(' ')
    # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                wordScore = getWordScore(word, n)
                totalScore += wordScore
                print('"' + word + '"' + ' earned ' + str(wordScore) +
                      ' points. Total: ' + str(totalScore) + ' points')
                print(' ')
    # Update the hand
                nHand = updateHand(nHand, word)
                newN = calculateHandlen(nHand)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if newN == 0:
        print('Run out of letters. Total score: ' +
              str(totalScore) + ' points.')
        print(' ')
    else:
        print('Goodbye! Total score: ' + str(totalScore) + ' points.')
        print(' ')


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
