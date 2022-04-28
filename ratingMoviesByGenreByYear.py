import warnings
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from dataProcessing import DataProcessing
from handle_db import HandleDB

# What is the number of films evaluated by genre in relation to the year of premiere?

class RatingMoviesByGenreByYear(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.ratingMoviesByGenreByYear = pd.DataFrame()
        self.top_generos = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.tableList_df)
            self.dataProcessed.uniqueItemsFilter("genres")

            genre_count = []

        for item in self.dataProcessed.items_list: # Agora fazemos a contagem
            consulta = 'SELECT COUNT(*) COUNT FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND premiered <= 2022'
            resultado = self.callTable(consulta)
            genre_count.append(resultado['COUNT'].values[0])

        # Prepara o dataframe
        self.ratingMoviesByGenreByYear['genre'] = self.dataProcessed.items_list
        self.ratingMoviesByGenreByYear['Count'] = genre_count

        # Calcula os top 5
        self.ratingMoviesByGenreByYear = self.ratingMoviesByGenreByYear[self.ratingMoviesByGenreByYear['genre'] != 'n']
        self.ratingMoviesByGenreByYear = self.ratingMoviesByGenreByYear.sort_values(by = 'Count', ascending = False)
        self.top_generos = self.ratingMoviesByGenreByYear.head()['genre'].values

    def plot(self):
        
        plt.figure(figsize = (16,8))
        
        for item in self.top_generos:
            consulta = 'SELECT COUNT(*) Number_of_movies, premiered Year FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND Year <=2022 GROUP BY Year'
            result = self.callTable(consulta)
            plt.plot(result['Year'], result['Number_of_movies'])

        plt.xlabel('\nYear')
        plt.ylabel('Number of Movie Evaluated')
        plt.title('\nNumber of Movie Evaluated by Genre in relation of the Premiere Year\n')
        plt.legend(labels = self.top_generos)
        plt.show()