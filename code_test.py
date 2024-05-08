from slpp import slpp as lua

def parse_lua_file(lua_file):
    with open(lua_file, 'r') as file:
        return lua.decode(file.read())


lua_file_path = "data_test.lua"  # Remplacez cela par le chemin de votre fichier Lua
tableau_de_donnees = parse_lua_file(lua_file_path)
print("Données extraites du fichier Lua :")
print(tableau_de_donnees)


