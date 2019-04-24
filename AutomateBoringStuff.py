print("I am thinking of a number between 1 and 20. \n")
import random
randomnum = random.randint(1,20)
for guesstaken in range(1,9):
    print("Take Guess\n")
    guess = int(input())
    if guess < randomnum:
        print("your guess is too low")
    elif guess > randomnum:
        print("your guess is too high")
    else:
        break
if guess == randomnum:
    print("Good Job! You guessed my number in " + str(guesstaken) + " guesses")
else:
    print("Nope. The number I was thinking of was "+str(randomnum))