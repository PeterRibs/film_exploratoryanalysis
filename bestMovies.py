import warnings
import seaborn as sns
from IPython.display import display

warnings.filterwarnings("ignore")
sns.set_theme(style = "whitegrid")

from handle_db import HandleDB

# What are the Top 10 Best Movies?

class BestMovies(HandleDB):

    def __init__(self, database, command):
        super().__init__(database)
        self.openConnectDB()
        best10 = self.callTable(command)
        display(best10)