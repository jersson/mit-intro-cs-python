def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]
##ex-01
def absValue(a):
    return abs(a)

applyToEach(testList, absValue)

##ex-02
def addValue(a):
    return a + 1

applyToEach(testList, addValue)

#ex-03
def squareValue(a):
    return a * a

applyToEach(testList, squareValue)
