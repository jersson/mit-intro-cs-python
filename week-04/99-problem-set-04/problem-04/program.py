def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    result = 0
    for item in hand.keys():
        result += hand[item]
    return result

hand = {'h':1, 'e':1, 'l':2, 'o':1}
print(calculateHandlen(hand))