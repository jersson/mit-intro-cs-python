animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print(animals)

print(animals['c'])

#print(animals['donkey']) --> error

print(len(animals))

animals['a'] = 'anteater'
print(animals['a'])

print(len(animals['a']))

print('baboon' in animals)

print('donkey' in animals.values())

print('b' in animals)

print(animals.keys())

del(animals['b'])
print(len(animals))

print(animals.values())