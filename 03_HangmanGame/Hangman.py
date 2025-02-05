import random
from collections import Counter

guessWords = '''apfel mango banane kiwi apfelsine orange weintraube melone mandarine birne zitrone kirsche erdbeere'''

guessWords = guessWords.split(' ')
# zufällige Auswahl eines Wortes aus der "guessWords" Liste
word = random.choice(guessWords)

if __name__ == '__main__':
    print('Rate nach dem gesuchten Wort! Tipp: Es geht um Obst.')

    for i in word:
        # um die ungefüllten Buchstabenfelder darzustellen
        print('_', end = ' ')
    print()

    playing = True
    # Liste um geratene Buchstaben zu speichern
    lettersGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0: # flag wird geupdatet wenn das Wort korrekt erraten wird
            print()
            chances -= 1

            try:
                guess = str(input('Gib eine Buchstaben zum raten ein:'))
            except:
                print('Gib nur einen Buchstaben ein!')
                continue

            # Validierung der Schätzung
            if not guess.isalpha():
                print('Nur einen BUCHSTABEN eingeben!')
                continue
            elif len(guess) > 1:
                print('Nur EINEN Buchstaben eingeben!')
                continue
            elif guess in lettersGuessed:
                print('Den Buchstaben hattest du schon.')
                continue

            # wenn ein Buchstabe richtig erraten wurde
            if guess in word:
                # k, speichert die Anzahl die der Buchstabe im Wort vorkommt
                k = word.count(guess)
                for _ in range(k):
                    lettersGuessed += guess # der Buchstabe wird so oft hinzugefügt wie er vorkommt

            # Ausgabe des Wortes
            for char in word:
                    if char in lettersGuessed and (Counter(lettersGuessed) != Counter(word)):
                        print(char, end=' ')
                        correct += 1
                    # Wenn der Nutzer alle Buchstaben erraten hat
                    # Oder der Nutzer das Wort erraten hat
                    elif Counter(lettersGuessed) == Counter(word):
                        # Das Spiel endet auch mit übrigen Chancen
                        print("Das Wort ist: ", end=' ')
                        print(word)
                        flag = 1
                        print('Herzlichen Glückwunsch, du hast gewonnen!')
                        # break für den For-Loop
                        break
                        # break für den While-Loop
                        break
                    else:
                        print('_', end=' ')

        # Wenn der Nutzer seine Chancen aufgebraucht hat
        if chances <= 0 and (Counter(lettersGuessed) != Counter(word)):
            print()
            print('Verloren! Versuchs nochmal...')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
            print()
            print('Murks! Versuchs nochmal.')
            exit()

