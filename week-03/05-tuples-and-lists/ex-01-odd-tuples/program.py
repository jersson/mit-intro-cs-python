def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    result = aTup[0::2]
    return result

input = ('I', 'am', 'a', 'test', 'tuple')
output = oddTuples(input)

print(output)