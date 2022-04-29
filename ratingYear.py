import warnings
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from dataProcessing import DataProcessing
from handle_db import HandleDB

# What is the Movie median rating in relation to the Premiere Year?

class ratingYear(HandleDB):
    
    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.yearList = []
        self.ratingsList = []
        self.dataProcessed = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.dataDB)
            self.medianCalculation(self.dataProcessed.dataTable)
            self.yearList = list(set(self.dataProcessed.dataTable['premiered']))

    def medianCalculation(self, dataframe):
        for year in set(dataframe['premiered']):
            self.ratingsList.append(np.median(dataframe[dataframe['premiered'] == year]['Rating']))

    def plot(self):
        plt.figure(figsize = (16,8))
        plt.plot(self.yearList, self.ratingsList)
        plt.xlabel('\nYear')
        plt.ylabel('Rating median')
        plt.title('\nRating median of Movies in relation to the Premiere Year\n')
        plt.show()