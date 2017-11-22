#!/Users/ericentrup/anaconda/bin/python2.7

import os
import argparse
from glob import glob

from Database import Database
from Utilities import Process
from Utilities import dynamicImport


class Apollo(object):
    def __init__(self, settings):
        self.version = '5.0'
        self.root = os.path.dirname(os.path.abspath(__file__))
        self.settings      = settings
        self.mcSuccess     = []
        self.mcFailed      = []
        self.tablesSuccess = []
        self.tablesFailed  = []
        
        self.database = self.connectDatabase(settings)

    
    def main(self):
        foundMCs     = self.findMCs(self.settings)
        foundTables  = self.findTables(self.root)
        loadedTables = self.loadTables(foundTables)
        
        processedMCs = self.processMCs(settings, foundMCs, loadedTables)
        
        
        params = [(mc,table) for mc in foundMCs for table in loadedTables]
        
        if self.settings.multiprocess:
            processed = processTables(foundMCs, loadedTables)
        else:
            processed = Process.standard(foundMCs, loadedTables)
            
        self.databaseCreate(loadedTables, self.database)
        self.databaseUpdate(processed, self.database)
        
        foundAnalysis  = self.findAnalysis(self.root)
        loadedAnalysis = self.loadAnalysis(foundAnalysis)
        if self.settings.multiprocess:
            processed = Process.multi(loadedAnalysis)
        
    def processMCs(self,settings,foundMCs,loadedTables):
        params = [(mc,)]
        
        
    def databaseUpdate(self, processed, database):
        processed.append(self._runSummary())
        for item in processed:
            name = 
            database.update(name, data)
        
    def databaseCreate(self, loadedTables, database):
        for table in loadedTables:
            name   = table.__module__
            schema = table.__dict__.items()
            schema.append(('mc','TEXT'))
            fields = ['{} {}'.format(a,b) for a,b in schema]
            
            database.create(name, ','.join(fields))
            
    def _runSummary(self):
        return ('name','data')
        
    
    def loadAnalysis(self,foundAnalysis):
        loadedAnalysis = []
        for analysis in foundAnalysis:
            try:
                loadedAnalysis.append(dynamicImport(analysis).Analysis())
            except:
                message = "WARNING: Analysis failed for {}"
                print message.format(os.path.basename(analysis))
                
        return loadedAnalysis
    
    
    def loadTables(self,foundTables):
        loadedTables = []
        for table in foundTables:
            tableName = os.path.basename(table)
            try:
                loadedTables.append(dynamicImport(table).Table())
                self.tableSuccess.append(tableName)
            except:
                self.tableFailed.append(tableName)
                
        return loadedTables
                
        
    def findAnalysis(self, root):
        analysis = glob(os.path.join(root, 'Analysis/*'))
        return filter(os.path.isdir, tables)
        
        
    def findTables(self,root):
        tables = glob(os.path.join(root, 'Tables/*'))
        return filter(os.path.isdir, tables)
        
    
    def findMCs(self,settings):
        #return glob(os.path.join(path, 'mc*'))
        return range(10)
        
            
    def connectDatabase(self,settings):
        dbPath = os.path.join(settings.output, 'Sqlite3.db')
        if settings.update and os.path.exists(dbPath):
            os.remove(dbPath)
            
        database = Database(path = dbPath)
        
        return database
    
    
    
if __name__ == "__main__":
    description = "Some text here"
    parser = argparse.ArgumentParser(description = description)
    parser.add_argument('-i',dest='input',default=os.getcwd(),help='text')
    parser.add_argument('-o',dest='output',default=os.getcwd(),help='text')
    settings = parser.parse_args()
    
    apollo = Apollo(settings)
    apollo.main()