import pandas as pd
from IPython.display import display

from handle_db import HandleDB

class SchemaVizualization(HandleDB):

    def __init__(self, database):
        super().__init__(database)

    def tableList(self, command):
        if self.connection == None:
            print("You have to connect to database first! Use the method 'openConnectDB'.")
        else:
            if self.dataDB is None:
                self.dataDB = self.callTable(command)
                print(self.dataDB)
            else:
                print(self.dataDB)

    def tableSchema(self):
        tableList_list = self.dataDB["Table_Name"].values.tolist()
        for table in tableList_list:
            queryTable = "PRAGMA TABLE_INFO({})".format(table)
            result = pd.read_sql_query(queryTable, self.connection)
            print("Esquema da tabela:", table)
            display(result)
            print("-"*100)
            print("\n")
        
    def printTableSchema(self): 
        if self.dataDB is None:
            self.tableList()
            self.tableSchema()
        else:
            self.tableSchema()