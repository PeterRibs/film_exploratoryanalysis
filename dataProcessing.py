import warnings
import seaborn as sns
import pandas as pd
from IPython.display import display
from sklearn.feature_extraction.text import CountVectorizer

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

class DataProcessing():
    
    def __init__(self, dataTable):
        self.dataTable = dataTable
        self.dataPercentual = pd.Series()
        self.data_df = None
        self.data_list = []

    def uniqueItemsFilter(self, itemFilter):
        self.dataTable[itemFilter] = self.dataTable[itemFilter].str.lower().values
        temp = self.dataTable[itemFilter].dropna()
        pattern = '(?u)\\b[\\w-]+\\b'
        vector = CountVectorizer(token_pattern = pattern, analyzer = 'word').fit(temp)
        bag_data = vector.transform(temp)
        dataUnique =  vector.get_feature_names()
        self.data_df = pd.DataFrame(bag_data.todense(), columns = dataUnique, index = temp.index)
        self.data_list = [genre for genre in dataUnique if len(genre) > 1]
        self.data_df = self.data_df.drop(columns = 'n', axis = 0)
        print("\n#### DataProcessing - uniqueItemsFilter (df) ####\n")
        print("-"*50)
        print("\n#### DataProcessing - uniqueItemsFilter (list) ####\n")
        print("-"*50)

    def percentual(self):
        if self.data_df is None:
            self.uniqueItemsFilter()
            print("Call method percentual again.")
        else:
            self.dataPercentual = 100 * pd.Series(self.data_df.sum()).sort_values(ascending = False) / self.data_df.shape[0]
            display("\n#### DataProcessing - percentual ####\n")
            print("-"*50)
            return self.dataPercentual

