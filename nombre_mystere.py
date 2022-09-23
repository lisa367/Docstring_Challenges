import random

nombre_mystere = random.randint(0, 100)
essais = 5
win = False

print("*** Le jeu du nombre mystere ***")
print(f"Il te reste {essais} essais")
# print("Nombre mystere: ", nombre_mystere)

while essais > 0:
    choix = input("Devine le nombre: ")
    essais -= 1
    if int(choix) == nombre_mystere:
        print(f"Bravo ! Le nombre mystère était bien {nombre_mystere} !")
        print(f"Tu as trouvé le nombre en {5 - essais} essais.")
        win = True
        essais = 0
    else:
        if int(choix) > nombre_mystere:
            print(f"Le nombre mystère est plus petit que {choix}")
        else:
            print(f"Le nombre mystère est plus grand que {choix}")
        print(f"Il te reste {essais} essais")

if essais == 0 and win == False:
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")

print("Fin du jeu.")
