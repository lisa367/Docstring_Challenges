from curses.ascii import isdigit


context = False

a = input("Entrez un premier nombre: ")
b = input("Entrez un deuxième nombre: ")

"""c = input("Entrez un premier nombre: ")
d = input("Entrez un deuxième nombre: ")"""

def somme(x, y):
    
    return int(x) + int(y)

"""if a.isdigit() and b.isdigit():
    print(somme(a, b))
else:
    print("Veuillez entrer deux nombres valides")
    print(somme(c, d))"""

while context == False:
    try:
        if a.isdigit() and b.isdigit():
            context = True
            print(f"Le résultat de l'addition de {a} avec {b} est égal à  {somme(a, b)}")
    except ValueError:
        print("Veuillez entrer deux nombres valides")
        if a.isdigit() and b.isdigit():
            print(somme(a, b))