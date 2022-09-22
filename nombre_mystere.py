import random

nombre_mystere = random.randint(0, 100)
essais = 0
win = False

while essais < 5 or win == False:
    choix = input("Devine le nombre: ")
    essais += 1
    if choix == nombre_mystere:
        win = True
        print(f"Bravo ! Le nombre mystère était bien {nombre_mystere} !")
        print(f"Tu as trouvé le nombre en {essais} essais.")
    else:
        print(f"Il te reste {essais} essais")

if essais == 5 and win == False:
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")

print("Fin du jeu.")
