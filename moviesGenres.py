import warnings
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from dataProcessing import DataProcessing
from handle_db import HandleDB

# What is the number of Movies by genre?

class moviesGenres(HandleDB):
    
    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.table_moviesGenres = None
        self.dataProcessed = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.dataDB)
            self.dataProcessed.uniqueItemsFilter('genres')
            self.table_moviesGenres = self.dataProcessed.percentual()
        else:
            self.table_moviesGenres = self.dataProcessed.percentual()

    def barPlot(self):
        plt.figure(figsize = (16,8))
        sns.barplot(x = self.table_moviesGenres.values, y = self.table_moviesGenres.index, orient = "h", palette = "terrain")
        plt.ylabel('Genres')             
        plt.xlabel("\nPercentual of Movies (%)")
        plt.title('\nMovies Number (Percentual) per Genres\n')
        plt.show()
