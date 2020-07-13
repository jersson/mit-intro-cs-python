x = (1, 2, (3, 'John', 4), 'Hi')

eval = x[0]
print(('x[0]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = x[2]
print(('x[2]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = x[-1]
print(('x[-1]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = x[2][2]
print(('x[2][2]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = x[2][-1]
print(('x[2][-1]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = x[-1][-1]
print(('x[-1][-1]: {0} value: {1}').format(str(type(eval)), str(eval)))

try:
    eval = x[-1][2]
    print(('x[-1][2]: {0} value: {1}').format(str(type(eval)), str(eval)))
except:
    print('x[-1][2]: <nonetype> value: error')

eval = x[0:1]
print(('x[0:1]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = x[0:-1]
print(('x[0:-1]: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = len(x)
print(('len(x): {0} value: {1}').format(str(type(eval)), str(eval)))

eval = 2 in x
print(('2 in x: {0} value: {1}').format(str(type(eval)), str(eval)))

eval = 3 in x
print(('3 in x: {0} value: {1}').format(str(type(eval)), str(eval)))

try:
    eval = x[0] = 8
    print(('x[0] = 8: {0} value: {1}').format(str(type(eval)), str(eval)))
except:
    print('x[0] = 8: <nonetype> value: error')
 
 # a new comment