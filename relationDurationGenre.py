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

class RelationDurationGenre(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.dataProcessed = None
        self.table_RelationDurationGenre = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.tableList_df)
            self.dataProcessed.uniqueItemsFilter("genres")
            self.dataProcessed.items_list

        # Calcula duração por gênero
        genre_runtime = []
        for item in self.dataProcessed.items_list:
            command = 'SELECT runtime_minutes Runtime FROM  titles  WHERE genres LIKE '+ '\''+'%'+item+'%'+'\' AND type=\'movie\' AND Runtime!=\'NaN\''
            result = self.callTable(command)
            genre_runtime.append(np.median(result['Runtime']))


        # Prepara o dataframe
        self.table_RelationDurationGenre = pd.DataFrame()
        self.table_RelationDurationGenre['genre'] = self.dataProcessed.items_list
        self.table_RelationDurationGenre['runtime'] = genre_runtime

        # Remove índice 18 (news)
        self.table_RelationDurationGenre = self.table_RelationDurationGenre.drop(index = 18)

        # Ordena os dados
        self.table_RelationDurationGenre = self.table_RelationDurationGenre.sort_values(by = 'runtime', ascending = False)

    def plot(self): # Plot

        # Tamanho da figura
        plt.figure(figsize = (16,8))

        # Barplot
        sns.barplot(y = self.table_RelationDurationGenre.genre, x = self.table_RelationDurationGenre.runtime, orient = "h")

        # Loop
        for i in range(len(self.table_RelationDurationGenre.index)):
            plt.text(self.table_RelationDurationGenre.runtime[self.table_RelationDurationGenre.index[i]],
                    i + 0.25,
                    round(self.table_RelationDurationGenre["runtime"][self.table_RelationDurationGenre.index[i]], 2))

        plt.ylabel('Genre')             
        plt.xlabel('\nDuration median (Minutos)')
        plt.title('\nRelationship between Duration and Genre\n')
        plt.show()