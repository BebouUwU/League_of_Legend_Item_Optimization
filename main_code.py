###################################################################################

        # Code for optimazing the build path for league of legend #
# Using the datas on https://leagueoflegends.fandom.com/wiki/Module:ItemData/data #

###################################################################################

from slpp import slpp as lua
import pandas as pd

def parse_lua_file(lua_file):
    with open(lua_file, 'r') as file:
        return lua.decode(file.read())


lua_file_path = "data.lua" 
tableau_de_donnees = parse_lua_file(lua_file_path)

data = {"Item_Name" : tableau_de_donnees.keys()}

data = pd.DataFrame(data)

##########################
### Dataframe creation ###
##########################

mode = []
tier = []
cost = []

for item in tableau_de_donnees:
    colonne = tableau_de_donnees[item]

    mode.append(colonne.get("modes"))
    tier.append(colonne.get("tier"))
    cost.append(colonne.get("buy"))


#Getting the items statistics from the data
stat = [["Item_Name" ,"ad" ,"ah" ,"ap" ,"armor" ,"as" ,"crit" ,"critdamage" ,"hp" ,"hp5" ,"lifesteal" ,"mana" ,"mp5" ,"mr" ,"ms" ,"lethality" ,"mpenflat" ,"hsp" ,"omnivamp" ,"armpen" ,"mpen"]]  

for item in tableau_de_donnees:
    colonne = tableau_de_donnees[item]
    statistics = colonne.get("stats")
    if statistics != None :
        stat.append([item,statistics.get("ad"),statistics.get("ah"),statistics.get("ap"),statistics.get("armor"),statistics.get("as"),statistics.get("crit"),statistics.get("critdamage"),statistics.get("hp"),statistics.get("hp5"),statistics.get("lifesteal"),statistics.get("mana"),statistics.get("mp5"),statistics.get("mr"),statistics.get("ms"),statistics.get("lethality"),statistics.get("mpenflat"),statistics.get("hsp"),statistics.get("omnivamp"),statistics.get("armpen"),statistics.get("mpen")])

stat = pd.DataFrame(stat[1:],columns=stat[0])

data["mode"] = mode
data["tier"] = tier
data["cost"] = cost

data = pd.merge(data,stat,how='left') #Merging of the two dataframe

#################
# Data modeling #
#################

#We only keep the items with "Classic 5v5" mode, tier 3
data.drop(data[data['tier'].isin([1])].index, inplace=True)
data.drop(data[data['tier'].isin([2])].index, inplace=True)
data.drop(data[data['tier'].isin([4])].index, inplace=True)
data.drop(data[data['mode'].isin([{'classic sr 5v5': False, 'aram': True, 'nb': True, 'arena': True},{'classic sr 5v5': False, 'aram': True, 'nb': True, 'arena': False},{'classic sr 5v5': False, 'aram': True, 'nb': False, 'arena': True},{'classic sr 5v5': False, 'aram': True, 'nb': False, 'arena': False},{'classic sr 5v5': False, 'aram': False, 'nb': True, 'arena': True},{'classic sr 5v5': False, 'aram': False, 'nb': True, 'arena': False},{'classic sr 5v5': False, 'aram': False, 'nb': True, 'arena': True},{'classic sr 5v5': False, 'aram': False, 'nb': False, 'arena': True}])].index, inplace=True)
data = data[pd.to_numeric(data['cost'], errors='coerce').notna()]


# Load the datas into an excel file
data.to_excel("loaded_data.xlsx",index = False)


# Now calculating the value of each point of statistic #