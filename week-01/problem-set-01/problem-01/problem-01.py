s = 'milagro'
message_base = 'Number of vowels:'
result = 0
for letter in s:
    if letter in 'aeiou':
        result += 1

print('Number of vowels: {}'.format(result))