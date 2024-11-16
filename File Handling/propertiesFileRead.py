#import
import sys
from jproperties import Properties

def display(props: Properties) -> None :
    if props is not None:
        #display all values
        items = props.items()
        for eachItem in items:
            print(eachItem)
        
        #access key value indiviudally
        for eachItem in items :
            print("{} = {}".format(eachItem[0] , eachItem[1].data) )
        
        #get individual values
        dbUser = props.get("db.user")
        print("the user is: " ,dbUser)

def readProps() -> None:
    """_summary_ Simple python script to read the porperties file
    """
    #get the object
    prop = Properties()
    try:
        with open("db-config.properties" , "rb" ) as configs :
            prop.load(configs) #load the configs into properties similar to pickle
            display(prop)
            
    except Exception as e :
        print(e , file=sys.stderr)
 
    return prop #returns property


def getConnection(prop: Properties) -> None :
   connection = None 
   url = prop.get("db.url")
   try:
       connection = Connector.connect(url = prop.get("db.url") , )
   except Exception as e:
       print(e)

def read($connect):
    
   except:
       .close()

def update()
if __name__ == "__main__" :
   prop =  readProps()
   getConnection(prop)