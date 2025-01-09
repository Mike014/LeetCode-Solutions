import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame: 
    # Filter the countries with area >= 3000000 or population >= 25000000
    #  and select the columns 'name', 'population', 'area'
    # Ther command below is equivalent to the following SQL query
    # Because of the request of the exercise, we have to use the OR operator
    # A country is big if:
    # it has an area of at least three million (i.e., 3000000 km2), or
    # it has a population of at least twenty-five million (i.e., 25000000).

    big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    result = big_countries[['name', 'population', 'area']]
    return result

print(big_countries(pd.read_csv('world.csv')))





# Filtrare i paesi grandi
# big_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]

# Selezionare le colonne richieste
# result = big_countries[['name', 'population', 'area']]

# Stampare il risultato
# print(result)
