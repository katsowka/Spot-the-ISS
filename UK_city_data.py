import pandas as pd

# saving world_cities.csv file as a Pandas dataframe
file = 'data/worldcities.csv'
df = pd.read_csv(file)

# making UK cities dataframe
uk_city_data = ( df[df["country"]=="United Kingdom"]
                [["city", "admin_name", "lat", "lng", "population"]]
                .set_index("city") )
uk_city_data.sort_index(inplace=True)

# as is, the index (set to city name) of the UK cities dataframe is not unique
# print(uk_city_data.index.is_unique)  # --> False
# print(uk_city_data.loc["Newport"])  # --> returns 3 cities (in different locations)

# choosing just cities with population over 50 000 to eliminate duplicates
uk_big_city_data = uk_city_data[uk_city_data["population"] > 50000]
print(uk_big_city_data.index.is_unique)  # --> True

# changing the UK cities dataframe to a dictionary with city name and location
dict = uk_big_city_data[["lat", "lng"]].to_dict(orient='index')  # (orient='split', index=False)