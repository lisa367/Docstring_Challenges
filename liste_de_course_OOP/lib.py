# Méthodes: ajouter, enlever, afficher, sauvegarder
import json
from pathlib import Path
from pprint import pprint

class Liste:
    def __init__(self, nom):
        self.nom = nom
        self.file_name = f"{nom}.json"
        self.working_directory = Path.cwd()

        with open(self.file_name, 'w') as file:
            json.dump([], file)

    def __post_init__(self):
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
        with open(self.file_name, 'r') as file:
            liste = json.load(file)
        print("*" * 15)
        print(f"{self.nom.capitalize()}:")
        for item in liste:
            pprint(item)


    def enlever(self, item):
        with open(self.file_name, 'r') as file:
            liste = json.load(file)
        indice = liste.find(item)
        liste.pop(indice)
        with open(self.file_name, 'w') as file:
            json.dump(file, liste)


    def vider(self):
        with open(self.file_name, "r") as file:
            liste = json.load(file)
        liste.clear()
        with open(self.file_name, 'w') as file:
            json.dump(self.file_name, liste)
    

    def sauvegarder(self, liste):
        self.working_directory.save()


    def delete_list(self):
        self.working_directory.joinpath(self.file_name).unlink()
        ###