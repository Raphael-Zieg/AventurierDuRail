import pandas as pd
import numpy as np

class CitiesSelection:
    def __init__(self):
        self.all_cities_df = self.get_cities_df(max_cities_per_country=15,min_pop=100000)
        self.megalopoles = self.get_cities_df(max_cities_per_country=2,min_pop=1000000)

    def get_cities_df(
        self,
        cities_path="./worldcities.csv",
        continent_path="./continents_country.csv",
        min_pop=100000,
        max_cities_per_country=15,
        continent=None,
    ):
        """Args :
            - cities_path : chemin vers le csv avec les villes
            - continent_path : chemin vers le csv reliant les pays au continent
            - min_pop : Nombre minimum de habitants dans une ville
            - max_cities_per_country : Nombre maximum de villes par pays
            - Continent (optional): Choix d'un continent en particulier parmis :
                ['Asia' 'Europe' 'Africa' 'South America' 'Oceania' 'North America']
        Return :
            - un DF avec les villes résultantes : ['city', 'lat', 'lng', 'population', 'country', 'continent']

        Source :
            - Données des villes : https://simplemaps.com/data/world-cities
            - Données des continents : https://data.enseignementsup-recherche.gouv.fr/explore/dataset/curiexplore-pays/table/

        """
        #
        worldcities = pd.read_csv(cities_path)
        continents_country = pd.read_csv(continent_path)

        worldcities.columns = worldcities.columns.str.replace('"', "")
        worldcities = worldcities.applymap(
            lambda x: x.replace('"', "") if isinstance(x, str) else x
        )

        merged_df = pd.merge(
            worldcities, continents_country, left_on="iso3", right_on="Code"
        )

        result_df = merged_df[
            ["city_ascii", "lat", "lng", "population", "Entity", "Continent"]
        ]
        result_df = result_df[result_df["population"] >= min_pop]
        result_df = result_df.sort_values(by="population", ascending=False)

        def top_N_cities(group):
            return group.head(max_cities_per_country)

        top_cities_by_country = (
            result_df.groupby("Entity").apply(top_N_cities).reset_index(drop=True)
        )

        top_cities_by_country.rename(
            columns={
                "city_ascii": "city",
                "Entity": "country",
                "Continent": "continent",
            },
            inplace=True,
        )
        # top_cities_by_country.to_csv("top_cities_by_country.csv", index=False) 

        return top_cities_by_country

        def _compute_distances(self,df):
            num_cities = len(df)
            distance_matrix = np.zeros((num_cities, num_cities))

            # Remplissage de la matrice avec les distances calculées
            for i in range(num_cities):
                distance_matrix[i, :] = self.__haversine(df['lat'].iloc[i],
                                                df['lng'].iloc[i],
                                                df['lat'].values,
                                                df['lng'].values)

            # Créer un DataFrame à partir de la matrice des distances pour l'affichage ou l'analyse ultérieure
            return pd.DataFrame(distance_matrix, 
                                    index=df['city'], 
                                    columns=df['city'],
                                    dtype="int")

        def __haversine(self,lat1, lon1, lat2, lon2):
            # Rayon de la Terre en km
            R = 6371.0

            # Conversion des coordonnées de degrés en radians
            lat1_rad, lon1_rad = np.radians(lat1), np.radians(lon1)
            lat2_rad, lon2_rad = np.radians(lat2), np.radians(lon2)

            # Différences de coordonnées
            dlat = lat2_rad - lat1_rad
            dlon = lon2_rad - lon1_rad

            # Formule Haversine
            a = np.sin(dlat/2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon/2)**2
            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

            # Distance en km
            distance = R * c
            return distance

