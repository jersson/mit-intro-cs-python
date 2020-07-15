s = 'azcbobobegghakl'
search = 'bob'
size = len(s)
i = 0
result = 0

while i < size - 2:
    if s[i:i+3] == search:
        result += 1
    i += 1
print('Number of times bob occurs is: {}'.format(result))