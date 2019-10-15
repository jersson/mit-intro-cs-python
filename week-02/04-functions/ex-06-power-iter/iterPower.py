def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    counter = 0
    while counter < exp:
        result  *= base
        counter += 1
    return result

print(iterPower(5, 3))
