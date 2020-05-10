low = 1
high = 100
print('Choose a number between {} and {}'.format(low, high))
input("Press ENTER to start the game")

guesses = 1
while True:
    print('\t Guess in the range of {} to {}.'.format(low,high))
    guess = low + (high - low) // 2
    high_low = input('My guess is {}. Should I guess higher or lower? '
                     'enter h or l, or c if my guess was correct: '.format(guess)).casefold()
    if high_low == 'h':
        low = guess + 1  # Guess higher
    elif high_low == 'l':
        print()  # Guess lower
        high = guess - 1
    elif high_low == 'c':
        print('I got it in {} guesses!'.format(guesses))
        break
    else:
        print('Enter h, l, or c.')

    guesses = guesses + 1
