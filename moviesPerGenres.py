import warnings
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from dataProcessing import DataProcessing
from handle_db import HandleDB

# What is the number of titles by genre?

class MoviesPerGenres(HandleDB):
    
    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.table_MoviesPerGenres = None
        self.dataProcessed = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.tableList_df)
            self.dataProcessed.uniqueItemsFilter('genres')
            self.table_MoviesPerGenres = self.dataProcessed.percentual()
        else:
            self.table_MoviesPerGenres = self.dataProcessed.percentual()

    def barPlot(self):
        plt.figure(figsize = (16,8))
        sns.barplot(x = self.table_MoviesPerGenres.values, y = self.table_MoviesPerGenres.index, orient = "h", palette = "terrain")
        plt.ylabel('Genres')             
        plt.xlabel("\nPercentual of Movies (%)")
        plt.title('\nNumber (Percentual) of Titles per Genres\n')
        plt.show()
