import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from handle_db import HandleDB
from dataProcessing import DataProcessing

# What is the Movie median rating by Genre?

class ratingGenre(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.table_ratingGenre = pd.DataFrame()

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.dataDB)
            self.dataProcessed.uniqueItemsFilter('genres')
            
            genre_counts = []
            genre_ratings = []

            for item in self.dataProcessed.items_list:
    
                command = ' SELECT COUNT(rating) FROM ratings JOIN titles ON ratings.title_id=titles.title_id WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' '
                result = self.callTable(command)
                genre_counts.append(result.values[0][0])
            
                command = ' SELECT rating FROM ratings JOIN titles ON ratings.title_id=titles.title_id WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' '
                result = self.callTable(command)
                genre_ratings.append(np.median(result['rating']))

            self.table_ratingGenre['genres'] = self.dataProcessed.items_list
            self.table_ratingGenre['count'] = genre_counts
            self.table_ratingGenre['rating'] = genre_ratings
                
            print(self.table_ratingGenre.head(20))
            print("-"*50)

        else:
            print("Data is processed!")
            
    def dropData(self, item, column):
        self.table_ratingGenre = self.table_ratingGenre.drop(self.table_ratingGenre.index[self.table_ratingGenre[column] == item])
    
    def sortData(self, item):
        self.table_ratingGenre = self.table_ratingGenre.sort_values(by = item, ascending = False)

    def barPlot(self):
        plt.figure(figsize = (16,10))
        sns.barplot(y = self.table_ratingGenre.genres, x = self.table_ratingGenre.rating, orient = "h")

        for i in range(len(self.table_Rtable_ratingGenreatingFilmsByGenre.index)):
            
            plt.text(4.0, 
                    i + 0.25, 
                    str(self.table_ratingGenre['count'][self.table_ratingGenre.index[i]]) + " filmes")
            
            plt.text(self.table_ratingGenre.rating[self.table_ratingGenre.index[i]],
                    i + 0.25,
                    round(self.table_ratingGenre["rating"][self.table_ratingGenre.index[i]],2))

        plt.ylabel('Genres')               
        plt.xlabel('Rating median')
        plt.title('\nMedian Rating By Gender\n')
        plt.show()