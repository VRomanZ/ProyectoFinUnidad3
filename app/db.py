from pymongo import MongoClient

class dbConnection():
    def __init__(self, npags):
        self.client = MongoClient("mongodb://localhost:27017")
        self.url = "https://rickandmortyapi.com/api/character?page="
        self.ctx = self.client['Rick_and_Morty']
        self.collection = self.ctx.Characters
        self.npags = npags






