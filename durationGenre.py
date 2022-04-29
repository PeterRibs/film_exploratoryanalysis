import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from handle_db import HandleDB
from dataProcessing import DataProcessing

# What is the relationship between duration and genre?

class DurationGenre(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.table_DurationGenre = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.dataDB)
            self.dataProcessed.uniqueItemsFilter("genres")
            self.dataProcessed.items_list

        genre_runtime = []
        for item in self.dataProcessed.items_list:
            command = 'SELECT runtime_minutes Runtime FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND Runtime!=\'NaN\''
            result = self.callTable(command)
            genre_runtime.append(np.median(result['Runtime']))

        self.table_DurationGenre = pd.DataFrame()
        self.table_DurationGenre['genre'] = self.dataProcessed.items_list
        self.table_DurationGenre['runtime'] = genre_runtime

        self.table_DurationGenre = self.table_DurationGenre.drop(index = 18)

        self.table_DurationGenre = self.table_DurationGenre.sort_values(by = 'runtime', ascending = False)

    def plot(self):

        plt.figure(figsize = (16,8))

        sns.barplot(y = self.table_DurationGenre.genre, x = self.table_DurationGenre.runtime, orient = "h")

        # Loop
        for i in range(len(self.table_DurationGenre.index)):
            plt.text(self.table_DurationGenre.runtime[self.table_DurationGenre.index[i]],
                    i + 0.25,
                    round(self.table_DurationGenre["runtime"][self.table_DurationGenre.index[i]], 2))

        plt.ylabel('Genre')             
        plt.xlabel('\nDuration median (Minutes)')
        plt.title('\nRelationship between Duration and Genre\n')
        plt.show()