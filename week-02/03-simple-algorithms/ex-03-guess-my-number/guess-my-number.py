print('Please think of a number between 0 and 100!')
input_answer = ''
begin = 0
end = 100
guess = int((begin + end) / 2)
while input_answer != 'c':
    print('Is your secret number ' + str(guess) + '?')
    input_answer = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if input_answer == 'l':
        begin = guess        
        guess = int((begin + end) / 2)
    elif input_answer == 'h':
        end = guess
        guess = int((begin + end) / 2)
    elif input_answer != 'c':
        print('Sorry, I did not understand your input.')
print("Game over. Your secret number was: " + str(guess))