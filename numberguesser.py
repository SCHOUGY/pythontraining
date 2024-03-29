import random

guess_taken = 0
question = "I am thinking of a number between 1-10: "
number = random.randint(1, 10)


def check_input():
    while True:
        try:
            guess = int(input(question))
        except ValueError:
            print("That's not a number")
            continue
        if 1 < guess > 10:
            print("I didn't ask for that, give me a number between 1-10")
            continue
        else:
            return guess


while guess_taken < 6:
    guess = check_input()
    if guess == number:
        guess_taken = guess_taken + 1
        print("You win!  " + str(guess_taken) + " attempts needed.")
        break
    else:
        guess_taken = guess_taken + 1
        print(f"Nope, try again. {guess_taken} attempts taken out of 6")
        continue
else:
    print(f"You lose! I was thinking of {number}")
