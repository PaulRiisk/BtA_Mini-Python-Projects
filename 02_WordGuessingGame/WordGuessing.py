import random

#Benutzdefinierte Begrüßung
name = input("Wie heißt du? ")
print(f"Super, dann viel Spaß, {name}!")

#Wordliste
words = ['baum', 'computer', 'sonne', 'flugzeug', 'tisch', 'kaffee', 'buch', 'musik', 'fahrrad', 'hund',
    'lampe', 'meer', 'zug', 'wolke', 'gitarre', 'tür', 'schlüssel', 'auto', 'telefon', 'brille',
    'wald', 'stuhl', 'kerze', 'haus', 'uhr', 'schokolade', 'kamera', 'blume', 'uboot', 'schatten']
word = random.choice(words)

print("Rate nach dem geheimen Wort!")

#Gamelogik
guesses = ''
turns = 12

while turns > 0:

    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("Du hast gewonnen!")
        print("Das Wort ist: ", word)
        break
    guess = input("Rate nach einem Buchstaben: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Falsch")
        print("Du hast noch", + turns, 'Versuche übrig!')

    if turns == 0:
        print("Du hast verloren!")
        print("Das Wort war: ", word)