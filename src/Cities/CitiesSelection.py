import pandas as pd
import numpy as np


class CitiesSelection:
    def __init__(self):
        self.all_cities_df = self.get_cities_df(max_cities_per_country=15, min_pop=100000)
        self.megalopoles = self.get_cities_df(max_cities_per_country=2, min_pop=1000000)
