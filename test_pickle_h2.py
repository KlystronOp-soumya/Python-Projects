from hashlib import md5
import prog
import os
import mpu
pickles = []       
for root,dirs,files in os.walk("./"):
    # root is the dir we are currently in, f the filename that ends on ...
    pickles.extend( (os.path.join(root,f) for f in files if f.endswith(".pickle")) )
pickles=str(pickles)
print(pickles)
#mpu.io.write('test.pkl', myhello)
unserialized_data = mpu.io.read('test.pickle')
s1=str(unserialized_data.runs)
s=md5(str.encode(unserialized_data.name)).hexdigest()
s1=md5(str.encode(s1)).hexdigest()
def test_s():
    assert s == "e783c7044c361cd2f88aefc5caf9b7c5"

def test_s1():
    assert s1 == "b7a782741f667201b54880c925faec4b"