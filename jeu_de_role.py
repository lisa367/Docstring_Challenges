import random

game_over = False

vie_joueur = 50
vie_ennemi = 50

potions = 3

while vie_joueur > 0 or vie_ennemi > 0:
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
    if choix == 1:
        attaque_joueur = random.randint(5, 10)
        attaque_ennemi = random.randint(5, 15)

        vie_joueur -= attaque_ennemi
        vie_ennemi -= attaque_joueur
    
    elif choix == 2:
        if potions > 0:
            utilisation_potions = random.randint(15, 50)
            vie_joueur += utilisation_potions
            potions -= 1
        else:
            print("Il ne reste plus de potions.")