# Afficher les options de modification de la liste
# Recupérer le choix de l'utilisateur
# Effectuer la modification
# Signaler à l'utilisateur que la modification a bien été effectuée

# Re-afficher les options
    # si l'option choisie est 'quitter' : arrêter le programme
    # sinon : recommencer le procédé précédent


options  = """ 1: Ajouter un élément dans la liste
2: Retier un élément de la liste
3: Afficher la lister
4: Vider la liste
5: Quitter"""

liste_de_course = []
choix = 0

while int(choix) != 5:
    print(options)
    choix = input("Vôtre choix: ")

    if int(choix) == 1:
        a_ajouter = input("Elément à ajouter dans la liste: ")
        if a_ajouter not in liste_de_course:
            liste_de_course.append(a_ajouter)
            print("Le nouvel élément a bien été ajouter")
        else:
            print("Cet élément se trouve déjà dans la liste")

    elif int(choix) == 2:
        a_retirer = input("Elément de la liste à retirer: ")
        if a_retirer in liste_de_course:
            liste_de_course.remove(a_retirer)
        else:
            print("Cet élément n'est pas dans la liste")

    elif int(choix) == 3:
        for i, item in enumerate(liste_de_course, 1):
            print(f"{i}. {item}")

    elif int(choix) == 4:
        liste_de_course.clear()
        print("La liste a bien été vidée")

    else:
        print("Veuillez rentrer un chiffre compris entre 1 et 5")