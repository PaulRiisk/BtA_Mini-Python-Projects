import random

in_range = int(input('Hey Willkommen! Gib irgendeine Zahl ein: '))

chances = (int(in_range*0.03))+5

print(f"Das ist ein Zahlen-Rate-Spiel.\nDu hast {chances} versuche die richtige Zahl zu erraten. Die Zahl liegt zwischen 0 und {in_range}. Los gehts!")

number_to_guess = random.randrange(in_range)

guess_counter = 0

while guess_counter < chances:
        guess_counter += 1
        my_guess = int(input('Gib deine Schätzung ein: '))

        if my_guess == number_to_guess:
            print(f'Die Zahl ist {number_to_guess} und du hast sie in {guess_counter} von {chances} Versuchen herausgefunden!')
            break

        elif guess_counter >= chances and my_guess != number_to_guess:
            print(f'Ohh mist! Die Zahl war {number_to_guess}, du hast es nicht geschafft!')

        elif my_guess > number_to_guess:
            print(f'Deine Schätzung ist zu hoch!')

        elif my_guess < number_to_guess:
            print(f'Deine Schätzung ist zu niedrig!')