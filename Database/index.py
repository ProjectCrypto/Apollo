
import sqlite3 
import pandas as pd

import Procedures

class Database(object):
    def __init__(self, path):
        self.database = os.path.join(path, 'Sqlite3.db')
        
        
    def create(self,table,fields):
        with sqlite3.connect(self.database) as conn:
            query = """
                CREATE TABLE IF EXISTS {}(
                    id INTEGER PRIMARY KEY,
                    {}
                )
            """
            conn.execute(query.format(table,fields))
    
 
    def update(self,table,data):
        with sqlite3.connect(self.database) as conn:
            data.to_sql(table, if_exists='append', index=False)
            
            
    def query(self,query):
        with sqlite3.connect(self.database) as conn:
            return pd.read_sql(query, con=conn)
    
    
    def get(self,procedure):
        query = Procedures.get(procedure, None)
        if query:
            return self.query(query)
        else:
            message = "WARNING: Failed to execute {}"
            print message.format(procedure)
    
    
    def tables(self):
        with sqlite3.connect(self.database) as conn:
            query = """
                SELECT name
                FROM sqlite_master
                WHERE type = 'table'
            """
            return pd.read_sql(query, con=conn)
        
            
    
    
    
    
    
    