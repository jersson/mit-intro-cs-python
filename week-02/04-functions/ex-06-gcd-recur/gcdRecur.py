def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # If b = 0, then the answer is a
    # Otherwise, gcd(a, b) is the same as gcd(b, a % b)
    result = 1
    if b == 0:
        result = a
    else:
        result = gcdRecur(b, a % b)
    return result

# gcd(2, 12) = 2
# gcd(6, 12) = 6
# gcd(9, 12) = 3
# gcd(17, 12) = 1

print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))