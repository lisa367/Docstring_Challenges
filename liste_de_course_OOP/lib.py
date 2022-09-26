# Méthodes: ajouter, enlever, afficher, sauvegarder
import json
import pathlib
from pprint import pprint

class Liste:
    def __init__(self, nom):
        self.nom = nom
        self.file_name = f"{nom}.json"

        with open(self.file_name, 'w') as file:
            json.dump([], file)

    def __repr__(self):
        return f"Liste: {self.nom}"

    def create_list(self):
        with open(self.file_name, 'w') as file:
            json.dump([], file)

    def ajouter(self, item):
        with open(self.file_name, 'r') as file:
            liste = json.load(file)
        liste.append(item)
        with open(self.file_name, 'w') as file:
            json.dump(liste, file, indent=4)

    def afficher(self, liste):
        pass

    def enlever(self, item):
        pass

    def vider(self):
        with open(self.file_name, "r") as file:
            liste = json.load(file)
        liste.clear()
        with open(self.file_name, 'w') as file:
            json.dump(self.file_name, liste)
    
    def sauvegarder(self, liste):
        pass

    def delete_list(self):
        pass