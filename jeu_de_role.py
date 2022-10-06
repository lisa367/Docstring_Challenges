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

        print(f"Vous avez infligé {attaque_joueur} points de dégâts à l'ennemi")
        print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégâts")

        print(f"Il vous restes {vie_joueur} points de vie")
        print(f"Il reste {vie_ennemi} points de vie à l'ennemi")

        print("-"*30)
    
    elif choix == 2:
        if potions > 0:
            utilisation_potions = random.randint(15, 50)
            vie_joueur += utilisation_potions
            potions -= 1

            print(f"Vous recupérez {utilisation_potions} points de vie")
        else:
            print("Il ne reste plus de potions.")


# Passer un tour
# transformer les attaques en fonctions ou en classes
def attaque_joueur():
    attaque_joueur = random.randint(5, 10)
    vie_ennemi -= attaque_joueur

def attaque_ennemi():
    attaque_ennemi = random.randint(5, 15)
    vie_joueur -= attaque_ennemi