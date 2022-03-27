"""
The StringIO module is an in-memory file-like object.
 This object can be used as input or output to the most function that would expect a standard file object. When the StringIO object is created it is initialized by passing a string to the constructor. If no string is passed the StringIO will start empty. 
In both cases, the initial cursor on the file starts at zero.
"""
from io import StringIO

string ='This is initial string.'
 
# Using the StringIO method to set
# as file object. Now we have an
# object file that we will able to
# treat just like a file.
file = StringIO(string)
 
# this will read the file
print(file.read())
 
# We can also write this file.
file.write(" Welcome to Hello World.")
 
# This will make the cursor at
# index 0.
file.seek(0)
 
# This will print the file after
# writing in the initial string.
print('The string after writing is:', file.read())
#Retrieve the entire content of the File
print(file.getvalue())
print("Is the file stream interactive?", file.isatty())
 
# This will returns whether the file is
# readable or not.
print("Is the file stream readable?", file.readable())
 
# This will returns whether the file supports
# writing or not.
print("Is the file stream writable?", file.writable())
 
# This will returns whether the file is
# seekable or not.
print("Is the file stream seekable?", file.seekable())
 
# This will returns whether the file is
# closed or not.
print("Is the file closed?", file.closed)
print(file.read())
 
# Hence to set the cursor position
# to read or write the file again
# we use seek().We can pass any index
# here form(0 to len(file))
file.seek(0)
 
# Now we can able to read the file again()
print(file.read())

# Here the cursor is at index 0.
print(file.tell())
 
# Cursor is set to index 20.
file.seek(20)
 
# Print the index of cursor
print(file.tell())

file.truncate(18) #drops all the contents after the cursor placed at 18th pos

print(file.read())

#close the file
file.close()
del file
