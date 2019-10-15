def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    if exp == 0:
        result = 1
    elif exp == 1:
        result = base
    else :
        result = base * recurPower(base, exp - 1)
    return result

print(recurPower(10, 0))
print(recurPower(10, 1))
print(recurPower(10, 2))
print(recurPower(5, 3))
