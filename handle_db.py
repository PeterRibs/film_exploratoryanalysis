import sqlite3
import pandas as pd

class HandleDB():
    def __init__(self, database):
        self.database = database
        self.connection = None
        self.tableList_df = None

    def openConnectDB(self):
        print("\nOpen the connection with %s\n" %(self.database))
        self.connection = sqlite3.connect(self.database)

    def closeConnectDB(self):
        if self.connection == None:
            print("Connection do not exist!")
        else:
            print("Close the connection with %s" %(self.database))
            self.connection.close()
            self.connection == None
    
    def callTable(self, callCommand):
        if self.connection == None:
            self.openConnectDB()

        self.tableList_df = pd.read_sql_query(callCommand, self.connection)
        return self.tableList_df