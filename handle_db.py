import sqlite3
import pandas as pd
from IPython.display import display

class HandleDB():
    def __init__(self, database):
        self.database = database
        self.connection = None
        self.tableList_df = None

    def openConnectDB(self): # Open connection with database
        print("\nOpen the connection with %s\n" %(self.database))
        self.connection = sqlite3.connect(self.database)

    def closeConnectDB(self): # Close connection with database
        if self.connection == None:
            print("Connection do not exist!")
        else:
            print("Close the connection with %s" %(self.db_name))
            self.connection.close()
            self.connection == None
    
    def callTable(self, callCommand):
        if self.connection == None:
            print("Connection do not exist!")
        else:
            self.tableList_df = pd.read_sql_query(callCommand, self.connection) # Extrai o resultado
            display("\n#### HandleDB - CallTable ####\n\n", self.tableList_df.head()) # Visualizing the head of the result
            print("-"*50)
            return self.tableList_df

