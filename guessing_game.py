number = 5
lives = 3

while lives > 0:
    answer = int(input('Guess number between 0 and 9: '))
    lives-=1
    if answer == number:
        print('You win!')
        break
    else:
        print('Try one more time!')