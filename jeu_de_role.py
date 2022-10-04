import random

game_over = False

vie_utilisateur = 50
vie_ennemi = 50

potions_utilisateur = 3

while vie_utilisateur > 0 or vie_ennemi > 0:
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")