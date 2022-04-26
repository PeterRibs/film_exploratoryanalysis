from handle_db import HandleDB
import pandas as pd
from IPython.display import display

class SchemaVizualization(HandleDB):

    def __init__(self, database):
        super().__init__(database)
        # self.command = input("SQL command: ")

    def tableList(self, command): # Extract a list of tables
        if self.connection == None:
            print("You have to connect to database first! Use the method 'openConnectDB'.")
        else:
            if self.tableList_df is None:
                self.tableList_df = self.callTable(command)
                print(self.tableList_df)
            else:
                print(self.tableList_df)

    def tableSchema(self):
        tableList_list = self.tableList_df["Table_Name"].values.tolist() # Converting dataframe in list
        for table in tableList_list: # Extract the schema of each table
            queryTable = "PRAGMA TABLE_INFO({})".format(table)
            result = pd.read_sql_query(queryTable, self.connection)
            print("Esquema da tabela:", table)
            display(result)
            print("-"*100)
            print("\n")
        
    def printTableSchema(self): 
        if self.tableList_df is None:
            self.tableList()
            self.tableSchema()
        else:
            self.tableSchema()


comando = "SELECT NAME AS 'Table_Name' FROM sqlite_master WHERE type = 'table'"

conn = SchemaVizualization("imdb.db")

conn.openConnectDB()

conn.tableList(comando)

conn.printTableSchema()