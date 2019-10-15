def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smaller = a
    result  = 1
    
    if a == b:
        result = a
    else:
        if a > b:
            smaller = b
        
        counter = 1
        while counter <= smaller:
            if a % counter == 0 and b % counter == 0:
                result = counter
            counter = counter + 1
    return result

# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1
print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))