###################################################################################

        # Code for optimazing the build path for league of legend #
# Using the datas on https://leagueoflegends.fandom.com/wiki/Module:ItemData/data #

###################################################################################

from slpp import slpp as lua
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

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
#data.to_excel("loaded_data.xlsx",index = False)
print(data)


# Searching the best build for maximazing a type of statistic #
def max_stat(statistic,data):
    if len(statistic) == 1:
        data_sort = data.sort_values(by=statistic, ascending = False)

        print("The best build for maximazing this statistic is : ",data_sort["Item_Name"][:5])
    else :
        new_stat = []
        for name in statistic:
            new_stat.append("new_"+name)
        data_rescaled = data.copy()

        scaler = MinMaxScaler()

        data_rescaled[new_stat] = scaler.fit_transform(data_rescaled[statistic])
        data_rescaled = data_rescaled.fillna(0)
        data_rescaled["Total"] = data_rescaled[new_stat].sum(axis = 1)
        data_rescaled = data_rescaled.sort_values(by='Total', ascending = False)
        print(data_rescaled.head())
        print("The best build for maximazing this statistic is : ")
        print(data_rescaled["Item_Name"][:5])


# Now calculating the value of each point of statistic #
# Using a MinMaxScaler (assuming that statistic has the same value but different amount) #
def best_item(data,cost = False):
    if cost == False:
        stat = ["ad" ,"ah" ,"ap" ,"armor" ,"as" ,"crit" ,"critdamage" ,"hp" ,"hp5" ,"lifesteal" ,"mana" ,"mp5" ,"mr" ,"ms" ,"lethality" ,"mpenflat" ,"hsp" ,"omnivamp" ,"armpen" ,"mpen"]
        new_stat = []
        for name in stat:
            new_stat.append("new_"+name)

        data_rescaled = data.copy()

        scaler = MinMaxScaler()

        data_rescaled[new_stat] = scaler.fit_transform(data_rescaled[stat])
        data_rescaled = data_rescaled.fillna(0)
        data_rescaled["Total"] = data_rescaled[new_stat].sum(axis = 1)
        data_rescaled = data_rescaled.sort_values(by='Total', ascending = False)
        print(data_rescaled.head())
        print("Best Items are : ")
        print(data_rescaled["Item_Name"][:5])
    elif cost == True:
        stat = ["ad" ,"ah" ,"ap" ,"armor" ,"as" ,"crit" ,"critdamage" ,"hp" ,"hp5" ,"lifesteal" ,"mana" ,"mp5" ,"mr" ,"ms" ,"lethality" ,"mpenflat" ,"hsp" ,"omnivamp" ,"armpen" ,"mpen"]
        new_stat = []
        for name in stat:
            new_stat.append("new_"+name)

        data_rescaled = data.copy()

        scaler = MinMaxScaler()

        data_rescaled[new_stat] = scaler.fit_transform(data_rescaled[stat])
        data_rescaled = data_rescaled.fillna(0)
        data_rescaled["Total"] = data_rescaled[new_stat].sum(axis = 1)
        data_rescaled["Item_Value"] = data_rescaled["Total"] / data_rescaled["cost"]
        data_rescaled = data_rescaled.sort_values(by='Item_Value', ascending = False)
        print(data_rescaled.head())
        print("Best Items are : ")
        print(data_rescaled["Item_Name"][:5])

best_item(data,cost=True)