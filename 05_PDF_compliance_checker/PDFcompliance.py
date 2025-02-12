# Modul mit Funktionen um ein Datenset(Hash) zu vergleichen
import hashlib

# Input Sequenzen vergleichen
from difflib import SequenceMatcher

def hash_file(fileName1, fileName2):

    # Mit Haslib den Hash abspeichern der Datei
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    with open(fileName1, "rb") as file:

        # Mit file.read() die Größe der Datei auslesen
        # lesen der Datei in kleinen Teilen
        # da große Dateien nicht gelesen werden können
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    with open(fileName2, "rb") as file:

        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

        # hexdigest( is of 160 bits
        return h1.hexdigest(), h2.hexdigest()

msg1, msg2 = hash_file("colorpalette.pdf ", "Linux-Sheet.pdf")

if msg1 != msg2:
    print("Diese Dateien sind nicht identisch.")
else:
    print("Die Dateien sind identisch.")