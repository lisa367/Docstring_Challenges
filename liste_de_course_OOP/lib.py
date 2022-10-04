# Méthodes: ajouter, enlever, afficher, sauvegarder
import json
from pathlib import Path
from pprint import pprint

class Liste:
    def __init__(self, nom):
        self.nom = nom
        self.file_name = f"{nom}.json"
        self.working_directory = Path.cwd()
        self.liste = []

        with open(self.file_name, 'w') as file:
            json.dump([], file)

    def __repr__(self):
        return f"Liste: {self.nom}"

    def __str__(self):
        return f"Cette liste est une liste de {self.nom}"


    def __del__(self):
        return f"La liste {self.nom} a été supprimée."


    def ajouter(self, item):
        if type(item) == list:
            self.liste.extend(item)
        else:
            self.liste.append(item)


    def afficher(self, liste):
        print("*" * 15)
        print(f"{self.nom.capitalize()}:")
        for item in self.liste:
            pprint(item)


    def enlever(self, item):
        indice = self.liste.find(item)
        self.liste.pop(indice)
        

    def vider(self):
        self.liste.clear()
        
    
    def sauvegarder(self, liste):
        data = self.working_directory / "data" / self.file_name
        with open(data, 'w') as file:
            json.dump(self.liste, file)


    def delete_list(self):
        # self.working_directory.joinpath(self.file_name).unlink()
        del self.liste
        

"""

    def create_list(self):
        with open(self.file_name, 'w') as file:
            json.dump([], file)

    def __post_init__(self):
        with open(self.file_name, 'w') as file:
            json.dump([], file)

    def ajouter(self, item):
        with open(self.file_name, 'r') as file:
            liste = json.load(file)
        liste.append(item)
        with open(self.file_name, 'w') as file:
            json.dump(liste, file, indent=4)
"""