import os

# Bestand in read-only (r) mode openen
bestand = open("klasgenoten.txt", "r")

# Een tekst naar het bestand schrijven
print(bestand.read())

# Vergeet bestand niet te sluiten!
bestand.close()
