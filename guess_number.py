from random import randint


number = randint(1,100)

print('Guess one!')

while True:
    guess = int(input('Enter your guess: '))

    if number == guess:
        print('The Winner!')
        break
    elif number > guess:
        print("It's bigger")
    else:
        print("It's smaller")