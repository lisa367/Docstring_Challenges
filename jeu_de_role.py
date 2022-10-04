import random

game_over = False

vie_joueur = 50
vie_ennemi = 50

potions_utilisateur = 3

while vie_joueur > 0 or vie_ennemi > 0:
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
    if choix == 1:
        attaque_joueur = random.randint(5, 10)
        attaque_ennemi = random.randint(5, 15)