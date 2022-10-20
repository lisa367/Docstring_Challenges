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

# conditions = validators()
condition = False
while condition == False:
    calcul = input("Veuillez entrer une opération : ").split(" ")
    # symbole = calcul.find(calcul[1])
    symbole = calcul[1]

    v1 = len(operation_liste) != 3
    v2 = (operation_liste[0].isdigit() and operation_liste[2].isdigit())
    v3 = symbole in operateurs

    if v1 and v2 and v3:
        condition = True

a, b = int(calcul[0]), int(calcul[2])

if symbole == operateurs[0]:
    print(a + b)
elif symbole == operateurs[1]:
    print(a - b)
elif symbole == operateurs[2]:
    print(a * b)
elif symbole == operateurs[3]:
    print(a / b)
elif symbole == operateurs[4]:
    print(a % b)


# Fonction de validation dess données:
    # deux nombres et un operateur séparés d'un espace
    # operation dans le bon ordre : regex

# Re-demander un input tant que la fonction de validation ne retourne pas True

# Effectuer l'opération adéquate selon l'opérateur et afficher le résultat dans le terminal

# split, in, eval, isdigit
