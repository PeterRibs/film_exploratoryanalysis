import warnings
import pycountry
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from handle_db import HandleDB
from dataProcessing import DataProcessing

# What is the number of movies produced per country?

class MoviesCountry(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.df_MoviesCountry = pd.DataFrame()

    def dataProcessing(self):

        # Listas auxiliares
        countryNames = []
        count = []

        # Loop para obter o país de acordo com a região
        for i in range(self.tableList_df.shape[0]):
            try:
                coun = self.tableList_df['region'].values[i]
                countryNames.append(pycountry.countries.get(alpha_2 = coun).name)
                count.append(self.tableList_df['Number_of_movies'].values[i])
            except: 
                continue

        # Prepara o dataframe
        self.df_MoviesCountry['country'] = countryNames
        self.df_MoviesCountry['Movie_Count'] = count

        # Ordena o resultado
        self.df_MoviesCountry = self.df_MoviesCountry.sort_values(by = 'Movie_Count', ascending = False)

    def barPlot(self):

        plt.figure(figsize = (20,8))

        sns.barplot(y = self.df_MoviesCountry[:20].country, x = self.df_MoviesCountry[:20].Movie_Count, orient = "h")

        for i in range(0,20):
            plt.text(self.df_MoviesCountry.Movie_Count[self.df_MoviesCountry.index[i]]-1,
                    i + 0.30,
                    round(self.df_MoviesCountry["Movie_Count"][self.df_MoviesCountry.index[i]],2))

        plt.ylabel('Countries')             
        plt.xlabel('\nNumber of Movies')
        plt.title('\nNumber of Movies per Country\n')
        plt.show()