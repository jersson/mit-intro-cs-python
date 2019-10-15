s = 'abcdeabcdexyz'
size = len(s)
i = 0
word = s[0]
last_word = ''
result = ''
while i < size - 1:
    if s[i] <= s[i + 1]:
        word = word + s[i + 1]
    else:
        if len(word) > len(last_word):
            last_word = word
        word = s[i + 1]
    i += 1

result = last_word
if len(word) > len(last_word):
    result = word
print(result)