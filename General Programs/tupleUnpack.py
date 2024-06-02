# unpack elements of a tuple
tup = (1,3,3,4,5,6)
a , b , *c = tup
a , *b , c = tup
print( 'a-',a,'b=', b , 'c=' , c)