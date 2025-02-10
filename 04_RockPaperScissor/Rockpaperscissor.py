import random
from time import sleep
# Wiedergabe der Spielanleitung
print('Gewinnregel des Spiels "Schere Stein Papier":\n'
      + "Stein vs Papier -> Papier gewinnt \n"
      + "Stein vs Schere -> Stein gewinnt \n"
      + "Papier vs Schere -> Schere gewinnt \n")

while True:
        print("Der Computer ist dran und entscheidet...")
        sleep(1)
        print("...fertig!\n")
        sleep(1)


        print("Du bist dran. Gib deine Auswahl ein: \n 1 - Stein \n 2 - Papier \n 3- Schere \n")

        # Nimm die Eingabe vom Nutzer
        choice = int(input("Gib deine Auswahl ein: "))

        # Validierung der Nutzereingabe
        while choice > 3 or choice < 1:
            choice = int(input('Gib eine valide Auswahl (Zahlen 1 bis 3) ein: '))

        # Initialisierung Wert von choice_name Variable korrespondiert zum choice value
        if choice == 1:
            choice_name = 'Stein'
        elif choice == 2:
            choice_name = 'Papier'
        else:
            choice_name = 'Schere'

        # Ausgabe Nutzerauswahl
        print('Deine Wahl ist: ', choice_name)
        sleep(1)

        # Der Computer wählt eine zufällige Zahl zwischen 1, 2 und 3
        comp_choice = random.randint(1, 3)

        # Initialisierung value comp_choice_name zum choice value
        if comp_choice == 1:
            comp_choice_name = 'Stein'
        elif comp_choice == 2:
            comp_choice_name = 'Papier'
        else:
            comp_choice_name = 'Schere'

        print('Die Computerauswahl ist: ', comp_choice_name)
        sleep(1)
        print(choice_name,'vs', comp_choice_name)
        sleep(2)

        # Bestimmen des Gewinners
        if choice == comp_choice:
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
            result = 'Papier'
        elif (choice == 1 and comp_choice ==3) or (comp_choice == 1 and choice == 3):
            result = 'Stein'
        elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
            result = 'Schere'

        # Ausgabe des Ergebnisses
        if result == "DRAW":
            print("<== Es ist ein Unentschieden! ==>")
        elif result == choice_name:
            print("<== Du hast gewonnen! ==>")
        else:
            print("<== Der Computer gewinnt! ==>")

        # Nochmal spielen Frage
        sleep(1)
        print("Möchtest du noch einmal spielen? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break

        # Nach dem Loop
        print("Danke fürs spielen!\n")