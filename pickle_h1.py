# Enter your code here. 
import pickle
import os
data={
  "a" : [5,9],
  "b":[5,6],
  "c" : ["Pickle is","helpful"]
}
#Dump file in pickle
try:
    with open("test.pkl","wb") as f:
      pickle.dump(data,f)
    
    #delete the data 
    del(data)
except Exception as e:
  print(e)

#Read data back from pickle
try:
    with open("test.pkl","rb") as f:
      dt=pickle.load(f)

    print(dt)
except Exception as e:
  print(e)
    

pickles = []       
for root,dirs,files in os.walk("./"):
    # root is the dir we are currently in, f the filename that ends on ...
    pickles.extend( (os.path.join(root,f) for f in files if f.endswith(".pkl")) )
pickles=str(pickles)
print(pickles)

with open('.hidden.txt','w') as outfile:
	outfile.write(pickles)




