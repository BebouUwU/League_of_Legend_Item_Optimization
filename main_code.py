###################################################################################

        # Code for optimazing the build path for league of legend #
# Using the datas on https://leagueoflegends.fandom.com/wiki/Module:ItemData/data #

###################################################################################

from slpp import slpp as lua
import pandas as pd

def parse_lua_file(lua_file):
    with open(lua_file, 'r') as file:
        return lua.decode(file.read())


lua_file_path = "data.lua"  # Remplacez cela par le chemin de votre fichier Lua
tableau_de_donnees = parse_lua_file(lua_file_path)

data = {"Item_Name" : tableau_de_donnees.keys()}

data = pd.DataFrame(data)

mode = []

for item in tableau_de_donnees:
    colonne = tableau_de_donnees[item]

    mode.append(colonne["modes"])

data["mode"] = mode

print(data)
