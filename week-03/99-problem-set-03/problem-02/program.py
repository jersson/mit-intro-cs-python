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

#TEST
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
#'_ pp_ e'