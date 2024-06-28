import random

def guess_the_number():
    # The computer selects a random number between 1 and 30
    number_to_guess = random.randint(1, 30)
    attempts = 0
    guessed_correctly = False
    lifeline = 5

    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 30.")
    print(f"You can only make {lifeline} attempts")

    while not guessed_correctly:
        try:
            # User inputs their guess
            user_guess = int(input("Enter your guess: "))
            
            # Increase the number of attempts
            attempts += 1
            lifeline -= 1
            print(f"Lifeline left: {lifeline}")

            # The user can only make 5 attempts to get the right number.
            if attempts <=  4:

                if user_guess < number_to_guess:
                    print("Too low! Try again.")

                elif user_guess > number_to_guess:
                    print("Too high! Try again.")

                else:
                    guessed_correctly = True
                    print(f"congratulations! You guessed the number in {attempts} attempts.")
            else:
                print("Game Over! Attempts exceeded")
                print(f"The number is {number_to_guess}")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Start the game
guess_the_number()
