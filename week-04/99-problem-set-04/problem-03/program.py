def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    result = False

    for item in wordList:
        if item == word:
            result = True
            sequence = getFrequencyDict(word)
            for letter in sequence.keys():
                result = result and (sequence[letter] <= hand.get(letter, 0))

            break

    return result

word = 'hello'
hand = {'h':1, 'e':1, 'l':2, 'o':1}
wordList = ('hello', 'hola', 'coffee')
print(isValidWord(word, hand, wordList))

word = 'hola'
print(isValidWord(word, hand, wordList))

word = ''
print(isValidWord(word, hand, wordList))

hand = {'h':1, 'e':1, 'l':2, 'o':1, 's':1}
word = 'hello'
print(isValidWord(word, hand, wordList))

hand = {'e': 2, 'u': 1, 'o': 1, 'c': 2, 'f': 3, 's': 1}
word = 'coffee'
wordList = ('coffee', 'hola')

print(isValidWord(word, hand, wordList))

