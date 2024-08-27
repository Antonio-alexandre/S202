from pokedex import Pokedex
from database import Database

def main():

    database = Database(database="pokedex", collection="pokemons")

    pokedex = Pokedex(database)

    # Filtra Pokémons por fraquezas
    weaknesses = ["Poison", "Grass"]
    pokedex.pokemonsByWeaknesses(weaknesses)

    # Filtra Pokémons por tipos
    types = ["Water", "Electric"]
    pokedex.pokemonsByTypes(types)

    #Filtra Pokémons por tipos que tem evolução
    ev = ["Dark", "Ghost"]
    pokedex.pokemonsByTypesThatHaveEvolutions(ev)

    # Filtra Pokémons por peso
    weight = "10.0 kg"
    pokedex.pokemonsByWeight(weight)

    # Filtra Pokémons por altura
    height = "0.71 m"
    pokedex.pokemonsByHeight(height)

if __name__ == "__main__":
    main()