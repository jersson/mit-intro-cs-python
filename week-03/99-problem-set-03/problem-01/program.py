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


#TEST
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))

secretWord = 'apple' 
lettersGuessed = ['e', 'p', 'l', 'a']
print(isWordGuessed(secretWord, lettersGuessed))