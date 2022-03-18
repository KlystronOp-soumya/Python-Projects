"""
This class implements a CRUD opeartion on MySQL
"""
from distutils.log import error
import re
import os,sys
from traceback import print_tb
import pymysql
from jproperties import Properties

class CRUDDemo:
    def __init__(self) -> None:
        pass

    @staticmethod
    def getDbConfig(configPath):
        #print(configPath)
        configs=Properties()
        dbProps={}
        try:
            with open(configPath,"rb") as dbConfig:
                configs.load(dbConfig)
            return configs
        except Exception as e :
            print("Here too")
            print(e)

    @staticmethod
    def getDbConn(dbConfigDict):    
        try:
            conn=pymysql.connect(host=dbConfigDict["db_url"].data,user=dbConfigDict["db_user"].data,
            password=dbConfigDict["db_password"].data,
            database=dbConfigDict["db_schema"].data)
            return conn

        except Exception as e:
            print("Here")
            print(e)

    @staticmethod
    def configResolver():

        properties=[]
        currentDir=os.getcwd()
        #print(currentDir)
        resourcesPath=currentDir+"\\resources"
        os.chdir(resourcesPath)
        #print(os.getcwd())
        try:

            for root,dirs,files in os.walk(os.getcwd()):
                for file in files:
                    if os.path.isfile(file) and (file.endswith(".properties")):
                        properties.append(os.path.join(root,file))
            for files in properties:
                if re.search(re.escape("db-config.properties"),files,re.I):
                    return files
        except Exception as e:
            print(e)

    @classmethod
    def createTable(cls,tableName=None):
        pass

    def searchById(self,id=None):
        pass

    def searchByName(self,name=None):
        pass
    def deleteRecordById(self,id=None):
        pass
    def updateRecordById(self,id=None,**kwargs):
        pass

if __name__ == "__main__":
    dbPropPath=CRUDDemo.configResolver()
    #print(dbPropPath)
    dbConfigDict = CRUDDemo.getDbConfig(dbPropPath)

    conn = CRUDDemo.getDbConn(dbConfigDict)
    if conn is not None:
       print("OK")
       conn.close()
    else:
       print("Error")
       conn.close()
