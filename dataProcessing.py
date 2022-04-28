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
        self.itemsPercentual = pd.Series()
        self.items_df = None
        self.items_list = []

    def uniqueItemsFilter(self, itemFilter):
        self.dataTable[itemFilter] = self.dataTable[itemFilter].str.lower().values
        temp = self.dataTable[itemFilter].dropna()
        pattern = '(?u)\\b[\\w-]+\\b'
        vector = CountVectorizer(token_pattern = pattern, analyzer = 'word').fit(temp)
        bag_items = vector.transform(temp)
        itemsUnique =  vector.get_feature_names()
        self.items_df = pd.DataFrame(bag_items.todense(), columns = itemsUnique, index = temp.index)
        self.items_list = [genre for genre in itemsUnique if len(genre) > 1]
        self.items_df = self.items_df.drop(columns = 'n', axis = 0)
        print("\n#### DataProcessing - uniqueItemsFilter (df) ####\n")
        print("-"*50)
        print("\n#### DataProcessing - uniqueItemsFilter (list) ####\n")
        print("-"*50)

    def percentual(self):
        if self.items_df is None:
            self.uniqueItemsFilter()
            print("Call method percentual again.")
        else:
            self.itemsPercentual = 100 * pd.Series(self.items_df.sum()).sort_values(ascending = False) / self.items_df.shape[0]
            display("\n#### DataProcessing - percentual ####\n")
            print("-"*50)
            return self.itemsPercentual

