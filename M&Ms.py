import random

print("------------------------")
print("    M&M guessing game!  ")
print("------------------------")

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("How manu M&Ms are in the jar? ")
    guess = int(guess_text)
    print(guess)

    if mm_count == guess:
        print(f"You got a free lunch! It was {guess}")
        break

    elif guess < mm_count:
        print("Sorry, that's to low...")

    else:
        print("That's too high!")

    attempts += 1

print(input(f"Bye, you're done in {attempts + 1} attempts."))
