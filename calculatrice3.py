# Calculatrice: Operations multiples


operateurs = ["+", "-", "*", "/", "%"]

#print("Veuillez entrer une opération : ")
operation = input("Veuillez entrer une opération : ")
operation_liste = operation.split("")

if len(operation_liste) != 3:
    print("Veuillez entrer une opération valide")

operateur = operateurs.find(operation_liste[1])


# Fonction de validation dess données:
    # deux nombres et un operateur séparés d'un espace
    # operation dans le bon ordre : regex

# Re-demander un input tant que la fonction de validation ne retourne pas True

# Effectuer l'opération et afficher le résultat dans le terminal

# split, in, eval, isdigit
