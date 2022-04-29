import warnings
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from dataProcessing import DataProcessing
from handle_db import HandleDB

# What is the number of Rated Movies by Genre in relation to the Premiere Year?

class RatingGenreYear(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.ratingGenreYear = pd.DataFrame()
        self.top_generos = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.dataDB)
            self.dataProcessed.uniqueItemsFilter("genres")

            genre_count = []

        for item in self.dataProcessed.items_list:
            consulta = 'SELECT COUNT(*) COUNT FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND premiered <= 2022'
            resultado = self.callTable(consulta)
            genre_count.append(resultado['COUNT'].values[0])

        self.ratingGenreYear['genre'] = self.dataProcessed.items_list
        self.ratingGenreYear['Count'] = genre_count

        self.ratingGenreYear = self.ratingGenreYear[self.ratingGenreYear['genre'] != 'n']
        self.ratingGenreYear = self.ratingGenreYear.sort_values(by = 'Count', ascending = False)
        self.top_genres = self.ratingGenreYear.head()['genre'].values

    def plot(self):
        
        plt.figure(figsize = (16,8))
        
        for item in self.top_genres:
            command = 'SELECT COUNT(*) Number_of_movies, premiered Year FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND Year <=2022 GROUP BY Year'
            result = self.callTable(command)
            plt.plot(result['Year'], result['Number_of_movies'])

        plt.xlabel('\nYear')
        plt.ylabel('Number of Movie Rated')
        plt.title('\nNumber of Movie Rated by Genre in relation of the Premiere Year\n')
        plt.legend(labels = self.top_genres)
        plt.show()