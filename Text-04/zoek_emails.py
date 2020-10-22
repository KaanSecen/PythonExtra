import re
import sys

emails = []

with open(sys.argv[1], "r") as bestand:

    regel = bestand.readline()
   
    while regel:

        # Vul de juiste regular expression voor een email in op de puntjes
        patroon = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

        # Gebruik de juiste code op de plaats van de puntjes
        gevonden = re.findall(patroon, regel)

        # Alle gevonden emails aan de email list toevoegen
        emails.extend(gevonden)
        
        # Volgende regel lezen
        regel = bestand.readline()

emails2 = ('\n'.join(emails))

print(emails2)

file = open("emailskom.txt", "w")
file.write(emails2)