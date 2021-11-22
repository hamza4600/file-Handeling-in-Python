

# open file from current folder

import os


aa=open("demo.txt")
print(aa.read())
 
#  there are serveral parametr in OPen() for reading writting and append the file
b=open("demo.txt","a")
bb=b.write("\n a new form of revolitation is comming to the world")
print(aa.read())

# window is not case senstive  c:\\home we will move to word home
# kinux is case senstive root/bin/env we will move in bin folder

# to get working directory
print(os.getcwd())
# to chnge  diectory r is used to raw form data 
def chdfolder():
    print(os.chdir(r"/home/hamza/Desktop"))
    print(os.getcwd())
    
chdfolder()    
#mkdir() is used to creat a folder 

# lsitdir() tell the files and folders 
def listDk():
    os.chdir(r"/home/hamza/Desktop")
    print(os.getcwd())
    print("\n list of folders is ")
    print(os.listdir())
listDk() 

# os.rmdir() amd dolder name in parametre it will delet the folder
    # isdir() return true or false it file exist or not isfile() stat() more infole of file
    
    #make a new file in current directory
def newf():
    qw=os.getcwd()
    filx='hamza.js'
    os.path.join(qw,filx)
    print(os.getcwd())     
newf()    

# use lgin
print(os.getlogin())
# system info system envirmnwetal info
print(os.environ.get("PATH"))

# os.system("program") will open the file we entre as argumnet
