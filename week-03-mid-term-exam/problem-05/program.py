# Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

# This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    result = dict()
    repeated = list()

    while len(aDict) > 0:
        item = aDict.popitem()
        value = item[1]
        values = aDict.values()
        
        if (value not in values and value not in repeated):
            result[item[0]] = item[1]
        else:
            repeated.append(value)

    return sorted(result)

# testDict = {1: 1, 2: 2, 3: 3}
# print(uniqueValues(testDict))

# testDict = {1: 1, 2: 1, 3: 1}
# print(uniqueValues(testDict))

# testDict = {1: 1}
# print(uniqueValues(testDict))

testDict = {}
print(uniqueValues(testDict))
