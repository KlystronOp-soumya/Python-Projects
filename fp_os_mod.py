import sys,os,io
from tokenize import String
from webbrowser import get

#function to get the current directory
def getCurrentDir()->String:
    s=os.getcwd()
    return s

#function to change current directory
def createNewDir():
    os.mkdir("New Folder")

def changeToDir():
    os.chdir(getCurrentDir()+"/New Folder")
    q=os.getcwd()
    return q