# Calculatrice: Operations multiples


operateurs = ["+", "-", "*", "/", "%"]

#print("Veuillez entrer une opération : ")
operation = input("Veuillez entrer une opération : ")
operation_liste = operation.split("")

operateur = operateurs.find(operation_liste[1])