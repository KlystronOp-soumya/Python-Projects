# Enter your code here.
import os
import pickle


class Player:
    def __init__(self, name    ,runs   ):
      self.name = name
      self.runs=runs
    
    
#Write code here to access value for name and runs from class PLayer    
myPlayer= Player("dhoni",10000)   
    
#Write code here to store the object in pickle file
try:
  with open("test.pickle","wb") as f:
    pickle.dump(myPlayer,f,protocol=pickle.HIGHEST_PROTOCOL)
except Exception as e:
  print(e)


del myPlayer

#Write code here to read the pickle file 
try:
  with open("test.pickle","rb") as f:
    player=pickle.load(f)
  
  print(player.name,player.runs,sep='\r\n')
except Exception as e:
  print(e)
