# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    result = True
    for letter in secretWord:
        result = letter in lettersGuessed
        if result == False:
            break
    
    return result



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''

    secretLetters = list(secretWord)
    for i in range(len(secretLetters)):
        if (secretLetters[i] not in lettersGuessed):
            secretLetters[i] = '_'
    
    result = ''.join(secretLetters)        

    return result


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    alphabet = string.ascii_lowercase

    lettersAlphabet = list(alphabet)
    for letter in lettersGuessed:
        if letter in lettersAlphabet:
            lettersAlphabet.remove(letter)
    
    result = ''.join(lettersAlphabet)
    
    return result    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    welcomeMessage = 'Welcome to the game, Hangman!'
    guessingMessage = 'I am thinking of a word that is 1 letter long.'
    splitterLine = '-------------'

    numberAttempts = 8
    attemptsLeftTemplate = 'You have {} guesses left.'
    avaliableLetters = string.ascii_lowercase
    availableLettersTemplate = 'Available letters: {}'
    inputMessage = 'Please guess a letter: '

    letters = list()
    lettersGuessed = list()

    if len(secretWord) > 1:
      guessingMessage = 'I am thinking of a word that is {} letters long.'.format(len(secretWord))

    print(welcomeMessage)
    print(guessingMessage)
    print(splitterLine)
    
    while numberAttempts > 0 :
      print(attemptsLeftTemplate.format(numberAttempts))
      print(availableLettersTemplate.format(avaliableLetters))
      letter = input(inputMessage).lower()
      
      if letter in letters:
        print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, letters)))
      else:
        letters.append(letter)

        if letter in secretWord:
          if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, letters)))
          else:
            lettersGuessed.append(letter)
            print('Good guess: {}'.format(getGuessedWord(secretWord, letters)))
        else:
          print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, letters)))
          numberAttempts -= 1
        
        avaliableLetters = getAvailableLetters(letters)
        
        if isWordGuessed(secretWord, lettersGuessed):
          print(splitterLine)
          print('Congratulations, you won!')
          break
      
      print(splitterLine)
    
    if numberAttempts == 0:
      print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))


    
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
