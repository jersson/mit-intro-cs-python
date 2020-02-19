animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest_item = ''
    max_len_item = 0
    
    for item in aDict:
        if len(aDict[item]) > max_len_item:
            biggest_item = item 

    return biggest_item

#test
print(biggest(animals))