# Méthodes: ajouter, enlever, afficher, sauvegarder
import json
import pathlib

class Liste:
    def __init__(self, nom):
        self.nom = nom

        with open(f"{self.nom}.json", 'w') as file:
            json.dump([], file)

    def __repr__(self):
        return self.nom

    def create_list(self):
        with open(f"{self.nom}.json", 'w') as file:
            json.dump([], file)

    def ajouter(self, item):
        with open(f"{self.nom}.json", 'r') as file:
            liste = json.load(file)
        liste.append(item)
        with open(f"{self.nom}.json", 'w') as file:
            json.dump(liste, file, indent=4)

    def afficher(self, liste):
        pass

    def enlever(self, item):
        pass
    
    def sauvegarder(self, liste):
        pass