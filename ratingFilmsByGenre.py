import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from handle_db import HandleDB
from dataProcessing import DataProcessing

# What is the median rating of films by genre?

class RatingFilmsByGenre(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.table_RatingFilmsByGenre = pd.DataFrame()

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.tableList_df)
            self.dataProcessed.uniqueItemsFilter('genres')
            
            genre_counts = []# Cria listas vazias
            genre_ratings = []# Cria listas vazias

            for item in self.dataProcessed.items_list: # Loop
    
                # Retorna a contagem de filmes por gênero
                command = ' SELECT COUNT(rating) FROM ratings JOIN titles ON ratings.title_id=titles.title_id WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' '
                result = self.callTable(command)
                genre_counts.append(result.values[0][0])
            
                # Retorna a avaliação de filmes por gênero
                command = ' SELECT rating FROM ratings JOIN titles ON ratings.title_id=titles.title_id WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' '
                result = self.callTable(command)
                genre_ratings.append(np.median(result['rating']))

            # Prepara o dataframe final
            self.table_RatingFilmsByGenre['genres'] = self.dataProcessed.items_list
            self.table_RatingFilmsByGenre['count'] = genre_counts
            self.table_RatingFilmsByGenre['rating'] = genre_ratings
                
            print(self.table_RatingFilmsByGenre.head(20))# Visualiza
            print("-"*50)


        else:
            print("Data is processed!")
            
    def dropData(self, item, column):
        self.table_RatingFilmsByGenre = self.table_RatingFilmsByGenre.drop(self.table_RatingFilmsByGenre.index[self.table_RatingFilmsByGenre[column] == item]) # Drop do índice 18 (news)
    
    def sortData(self, item):
        self.table_RatingFilmsByGenre = self.table_RatingFilmsByGenre.sort_values(by = item, ascending = False)

    def barPlot(self): # Plot
        plt.figure(figsize = (16,10))
        sns.barplot(y = self.table_RatingFilmsByGenre.genres, x = self.table_RatingFilmsByGenre.rating, orient = "h")

        for i in range(len(self.table_RatingFilmsByGenre.index)): # Textos do gráfico
            
            plt.text(4.0, 
                    i + 0.25, 
                    str(self.table_RatingFilmsByGenre['count'][self.table_RatingFilmsByGenre.index[i]]) + " filmes")
            
            plt.text(self.table_RatingFilmsByGenre.rating[self.table_RatingFilmsByGenre.index[i]],
                    i + 0.25,
                    round(self.table_RatingFilmsByGenre["rating"][self.table_RatingFilmsByGenre.index[i]],2))

        plt.ylabel('Genres')               
        plt.xlabel('Rating median')
        plt.title('\nMedian Rating By Gender\n')
        plt.show()