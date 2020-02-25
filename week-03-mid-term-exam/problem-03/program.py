def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    result = 0
    pot = b 
    while True:
        if pot * b <= x:
            pot *= b 
            result += 1
        else:
            if x > b:
                result += 1
            break
    return result

print(myLog(16, 2))
print(myLog(15, 3))
print(myLog(15, 3))
print(myLog(2, 9))
print(myLog(4, 16))


