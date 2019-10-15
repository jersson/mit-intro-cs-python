def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    result  = False
    size    = len(aStr)

    if size == 0:
        result = False
    elif size == 1:
        if char == aStr[0]:
            result = True
    else:
        begin   = 0
        end     = size - 1

        point   = int((begin + end) / 2)

        if aStr[point - 1] == char:
            result = True
        else:
            if aStr[point] > char:
                end = point
            else:
                begin = point
            result = isIn(char, aStr[begin: end])

    return result

print(isIn('a', 'abcdefghijklmnopqrstuvwxyz'))      #True
print(isIn('u', 'abcdefghijklmnopqrstuvwxyz'))      #True
print(isIn('u', 'abcdefghijklmnopqrst'))            #False
print(isIn('d', 'abbcdloqrruw'))                    #True
print(isIn('a', ''))                                #False