from curses.ascii import isdigit


context = False

def somme(x, y):
    return float(x) + float(y)


while context == False:
    try:
        a = input("Entrez un premier nombre: ")
        b = input("Entrez un deuxième nombre: ")
        #if a.isdigit() and b.isdigit():
        print(f"Le résultat de l'addition de {a} avec {b} est égal à  {somme(a, b)}")
        context = True
    except ValueError:
        print("Veuillez entrer deux nombres valides")