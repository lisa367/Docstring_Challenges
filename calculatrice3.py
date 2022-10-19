# Calculatrice: Operations multiples


operateurs = ["+", "-", "*", "/", "%"]

#print("Veuillez entrer une opération : ")
operation = input("Veuillez entrer une opération : ")
operation_liste = operation.split(" ")
operateur = operateurs.find(operation_liste[1])

def validators():
    verif1 = len(operation_liste) != 3
    verif2 = (operation_liste[0].isdigit() and operation_liste[2].isdigit())
    verif3 = operateur in operateurs
    # print("Veuillez entrer une opération valide")

    return verif1 and verif2 and verif3




# Fonction de validation dess données:
    # deux nombres et un operateur séparés d'un espace
    # operation dans le bon ordre : regex

# Re-demander un input tant que la fonction de validation ne retourne pas True

# Effectuer l'opération et afficher le résultat dans le terminal

# split, in, eval, isdigit
