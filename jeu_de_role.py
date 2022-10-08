import random

game_over = False

vie_joueur = 50
vie_ennemi = 50

potions = 3

def attaque_joueur():
    attaque_joueur = random.randint(5, 10)
    vie_ennemi -= attaque_joueur

    return attaque_joueur, vie_ennemi

def attaque_ennemi():
    attaque_ennemi = random.randint(5, 15)
    vie_joueur -= attaque_ennemi

    return attaque_ennemi, vie_joueur

while vie_joueur > 0 or vie_ennemi > 0:
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")
    saute_un_tour = False
    if choix == 1:
        if saute_un_tour:
            attaque_ennemi()
        else:
            attaque_joueur()
            attaque_ennemi()

        attaque_joueur = random.randint(5, 10)
        attaque_ennemi = random.randint(5, 15)

        vie_joueur -= attaque_ennemi
        vie_ennemi -= attaque_joueur

        if saute_un_tour == False:
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


    """        attaque_joueur = random.randint(5, 10)
        attaque_ennemi = random.randint(5, 15)

        vie_joueur -= attaque_ennemi
        vie_ennemi -= attaque_joueur

        print(f"Vous avez infligé {attaque_joueur} points de dégâts à l'ennemi")
        print(f"L'ennemi vous a infligé {attaque_ennemi} points de dégâts")

        print(f"Il vous restes {vie_joueur} points de vie")
        print(f"Il reste {vie_ennemi} points de vie à l'ennemi")

    """

    class Attaque:
        def __init__(self, attaquant, vie_cible, minimum, maximum):
            self.attaquant = attaquant
            self.vie_cible = vie_cible
            self.minimum = minimum
            self.maximum = maximum
        
        def attaquer(self):
            attaque = random.randint(self.minimum, self.maximum)
            self.vie_cible -= attaque

            return attaque, self.vie_cible