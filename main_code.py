###################################################################################

        # Code for optimazing the build path for league of legend #
# Using the datas on https://leagueoflegends.fandom.com/wiki/Module:ItemData/data #

###################################################################################

from pyparsing import nestedExpr


def parse_lua_file(lua_file):
    with open(lua_file, 'r') as file:
        lua_data = file.read()
        parsed_data = nestedExpr('{', '}').parseString(lua_data).asList()
        return parsed_data[0] if parsed_data else []

# Exemple d'utilisation
if __name__ == "__main__":
    lua_file_path = "data"  # Remplacez cela par le chemin de votre fichier Lua
    tableau_de_donnees = parse_lua_file(lua_file_path)
    print("Données extraites du fichier Lua :")
    print(tableau_de_donnees)
