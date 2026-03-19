import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")

## create variable "data" that represents the enitre pokedex list


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

# For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

data = json.load(pokedex)


""" def find_name(id):
    lang_choice = input("What language do you prefer? English, Japanese, Chinese, or French")
    if lang_choice == "English":
        for count in range(id):
            print(data[count]["name"]["english"])
    elif lang_choice == "Japanese":
        for count in range(id):
            print(data[count]["name"]["japanese"])
    elif lang_choice == "Chinese":
        for count in range(id):
            print(data[count]["name"]["chinese"])
    elif lang_choice == "French":
        for count in range(id):
            print(data[count]["name"]["french"])
find_name(data[-1]["id"]) """


""" def find_type(id):
    
    poke_type = input("Search for pokemon type")
    for count in range(id):
        if poke_type in data[count]["type"]:
            print(data[count]["name"])
find_type(data[-1]["id"]) """

def poke_search()