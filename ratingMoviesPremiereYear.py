import warnings
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import cm
import matplotlib.pyplot as plt
from IPython.display import display

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from dataProcessing import DataProcessing
from handle_db import HandleDB

# What is the median rating median of movies in relation to the premiere year?

class RatingMoviesPremiereYear(HandleDB):
    
    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.yearList = []
        self.ratingsList = []
        self.dataProcessed = None

    def dataProcessing(self):
        if self.dataProcessed is None:
            self.dataProcessed = DataProcessing(self.tableList_df)
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
        plt.title('\nRating median of movies in relation to the premiere year\n')
        plt.show()