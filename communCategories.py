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

class CommunCategory(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        self.callTable(command)
        self.table_CommunCategory = None

    def percentual(self):
        self.dataDB['percentual'] = (self.dataDB['COUNT'] / self.dataDB['COUNT'].sum()) * 100 # Percental of each category
        display("\n#### CommunCategory - Percentual ####\n")
        print("-"*50)
        return self.dataDB

    def filterPercentual(self, percentual):
        others = {}
        others['COUNT'] = self.dataDB[self.dataDB['percentual'] < percentual]['COUNT'].sum()
        others['percentual'] = self.dataDB[self.dataDB['percentual'] < percentual]['percentual'].sum()
        others['type'] = 'others'
        self.table_CommunCategory = self.dataDB[self.dataDB['percentual'] > percentual]
        self.table_CommunCategory = self.table_CommunCategory.append(others, ignore_index = True)
        self.table_CommunCategory = self.table_CommunCategory.sort_values(by = 'COUNT', ascending = False)
        print("-"*50)

    def piePlot(self):
        labels = [str(self.table_CommunCategory['type'][i])+' '+'['+str(round(self.table_CommunCategory['percentual'][i],2)) +'%'+']' for i in self.table_CommunCategory.index]

        cs = cm.Set3(np.arange(100))

        f = plt.figure()
        plt.pie(self.table_CommunCategory['COUNT'], labeldistance = 1, radius = 3, colors = cs, wedgeprops = dict(width = 0.8)) # Pie Plot
        plt.legend(labels = labels, loc = 'center', prop = {'size':6})
        plt.title("Titles distribution", loc = 'Center', fontdict = {'fontsize':10,'fontweight':10})
        plt.savefig('communCategories.png')
        plt.show()