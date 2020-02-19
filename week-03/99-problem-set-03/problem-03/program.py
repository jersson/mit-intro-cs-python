import string

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

#TEST
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
# print('abcdfghjlmnoqtuvwxyz')
