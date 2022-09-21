# Afficher les options de modification de la liste
# Recupérer le choix de l'utilisateur
# Effectuer la modification
# Signaler à l'utilisateur que la modification a bien été effectuée

# Re-afficher les options
    # si l'option choisie est 'quitter' : arrêter le programme
    # sinon : recommencer le procédé précédent

import sys


options  = """1: Ajouter un élément dans la liste
2: Retier un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter"""

liste_de_course = []
choix = 0
context = False

while context == False:
    print(options)
    print("\n")
    choix = input("Votre choix: ")

    if int(choix) == 1:
        a_ajouter = input("Entrez le nom d'un élément à ajouter dans la liste: ")
        if a_ajouter not in liste_de_course:
            liste_de_course.append(a_ajouter)
            print(f"L'élément {a_ajouter} a bien été ajouté à la liste.")
            print("*"*15)
            print("\n")
        else:
            print(f"L'élément {a_ajouter} se trouve déjà dans la liste.")
            print("*"*15)
            print("\n")

    elif int(choix) == 2:
        a_retirer = input("Entrez le nom d'un élément à retirer de la liste: ")
        if a_retirer in liste_de_course:
            liste_de_course.remove(a_retirer)
            print(f"L'élément {a_retirer} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {a_retirer} n'est pas dans la liste.")

    elif int(choix) == 3:
        if liste_de_course:
            print("\n")
            print("*"*15)
            print("Voici le contenu de votre liste:")
            for i, item in enumerate(liste_de_course, 1):
                print(f"{i}. {item}")
            print("*"*15)
            print("\n")
        else:
            print("Votre liste ne contient aucun élément.")
            print("*"*15)
            print("\n")

    elif int(choix) == 4:
        liste_de_course.clear()
        print("Votre liste a bien été vidée de son contenu.")
        print("*"*15)
        print("\n")

    elif int(choix) == 5:
        print("A bientôt !")
        context = True

    else:
        print("Veuillez rentrer un chiffre compris entre 1 et 5")
        print("*"*15)
        print("\n")

sys.exit()