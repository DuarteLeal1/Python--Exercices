import random

random_number = random.randint(1, 100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("Whats your attempt? ")
    guess = int(guess_text)
    print(guess)

    if random_number == guess:
        print(f"Nice! It was {guess}")
        break

    elif guess < mm_count:
        print("Sorry, that's to low...")

    else:
        print("That's too high!")

    attempts += 1

print(input(f"Bye, you're done in {attempts + 1} attempts."))
