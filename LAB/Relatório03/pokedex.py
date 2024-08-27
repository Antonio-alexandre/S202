from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def pokemonsByTypes(self, types: list):
        r = list(self.db.collection.find({"types": {"$in": types}}))
        writeAJson({"query": "pokemonsByTypes", "types": types, "result": r}, "logPokemonsByTypes.json")
        return r

    def pokemonsByTypesThatHaveEvolutions(self, types: list):
        r = list(self.db.collection.find({ "type": {"$in": types}, "next_evolution": {"$exists": True} }))
        writeAJson({"query": "pokemonsByTypesThatHaveEvolutions", "types": types, "result": r}, "logPokemonsByTypesThatHaveEvolutions.json")
        return r

    def pokemonsByWeight(self, weight: str):
        r = list(self.db.collection.find({"weight": {"$in": [weight]}}))
        writeAJson({"query": "pokemonsByWeight", "weight": weight, "result": r}, "logPokemonsByWeight.json")
        return r

    def pokemonsByHeight(self, height: str):
        r = list(self.db.collection.find({"height": {"$in": [height]}}))
        writeAJson({"query": "pokemonsByHeight", "height": height, "result": r}, "logPokemonsByHeight.json")
        return r

    def pokemonsByWeaknesses(self, weaknesses: list):
        r = list(self.db.collection.find({"weaknesses": {"$in": weaknesses}}))
        writeAJson({"query": "pokemonsByWeaknesses", "weaknesses": weaknesses, "result": r}, "logPokemonsByWeaknesses.json")
        return r