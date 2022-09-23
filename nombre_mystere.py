import random

nombre_mystere = random.randint(0, 100)
essais = 5
win = False

while essais > 0:
    choix = input("Devine le nombre: ")
    essais -= 1
    if choix == nombre_mystere:
        win = True
        print(f"Bravo ! Le nombre mystère était bien {nombre_mystere} !")
        print(f"Tu as trouvé le nombre en {essais} essais.")
    else:
        if choix > nombre_mystere:
            print(f"Le nombre mystère est plus grand que {choix}")
        else:
            print(f"Le nombre mystère est plus petit que {choix}")
        print(f"Il te reste {essais} essais")

if essais == 0 and win == False:
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")

print("Fin du jeu.")
