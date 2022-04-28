import warnings
import numpy as np
import seaborn as sns
from matplotlib import cm
import matplotlib.pyplot as plt
from IPython.display import display

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from handle_db import HandleDB

### What are the Most Common Movie Categories on IMDB?

class MoreCommunCategory(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.table_MoreCommunCategory = None

    def percentual(self):
        self.tableList_df['percentual'] = (self.tableList_df['COUNT'] / self.tableList_df['COUNT'].sum()) * 100 # Percental of each category
        display("\n#### MoreCommunCategory - Percentual ####\n")
        print("-"*50)
        return self.tableList_df

    def filterPercentual(self, percentual):
        others = {}
        others['COUNT'] = self.tableList_df[self.tableList_df['percentual'] < percentual]['COUNT'].sum() # Filter by percentual and sum
        others['percentual'] = self.tableList_df[self.tableList_df['percentual'] < percentual]['percentual'].sum()
        others['type'] = 'others' # Ajust the name
        self.table_MoreCommunCategory = self.tableList_df[self.tableList_df['percentual'] > percentual] # Filter the dataframe
        self.table_MoreCommunCategory = self.table_MoreCommunCategory.append(others, ignore_index = True) # Append with dataframe
        self.table_MoreCommunCategory = self.table_MoreCommunCategory.sort_values(by = 'COUNT', ascending = False) # Sort the result
        display("\n#### MoreCommunCategory - FilterPercentual ####\n")
        print("-"*50)

    def piePlot(self):
        labels = [str(self.table_MoreCommunCategory['type'][i])+' '+'['+str(round(self.table_MoreCommunCategory['percentual'][i],2)) +'%'+']' for i in self.table_MoreCommunCategory.index] # Ajust the labels

        cs = cm.Set3(np.arange(100)) # Colors: https://matplotlib.org/stable/tutorials/colors/colormaps.html

        f = plt.figure()
        plt.pie(self.table_MoreCommunCategory['COUNT'], labeldistance = 1, radius = 3, colors = cs, wedgeprops = dict(width = 0.8)) # Pie Plot
        plt.legend(labels = labels, loc = 'center', prop = {'size':6})
        plt.title("Titles distribution", loc = 'Center', fontdict = {'fontsize':10,'fontweight':10})
        plt.savefig('moreCommunCategories.png')
        plt.show()