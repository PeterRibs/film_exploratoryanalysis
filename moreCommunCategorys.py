from handle_db import HandleDB
from IPython.display import display
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

### What are the Most Common Movie Categories on IMDB?

class MoreCommunCategory(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.table_MoreCommunCategory = None

    def percentual(self):
        self.tableList_df['percentual'] = (self.tableList_df['COUNT'] / self.tableList_df['COUNT'].sum()) * 100 # Percental of each category
        display("\n#### MoreCommunCategory - Percentual ####\n\n", self.tableList_df)
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
        display("\n#### MoreCommunCategory - FilterPercentual ####\n\n", self.table_MoreCommunCategory) # Visualize
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
        


command= '''SELECT type, COUNT(*) AS COUNT FROM titles GROUP BY type''' 
a = MoreCommunCategory("imdb.db", command)
a.percentual()
a.filterPercentual(5)
a.piePlot()