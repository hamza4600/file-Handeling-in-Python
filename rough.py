import os


print(os.getcwd())
print(os.listdir())

# code is used to creat a file as we want write  in a functions
def Nfile():
    with open("hamza.js","w") as f:
        f.write("console.log(`hamza Khan`)")
        
# Nfile()

# detaIL OS OPERATING SYSTEM
print(os.uname())
     
        #list of process 
print(os.getegid())
        # usename
print(os.getlogin())        
#  os name
print(os.uname())


#function that copy word lendth greater than 4 and add then in a array and render that 
def four():
    f=open("demo.txt")
    val=f.read()
    line=val.split()
    count=0
    for i in  line:
        if len(i)<4:
            print(i)
            count+=1
        else:
            pass
        print("total number of wors greater than 4 are ",count)
four()         

# function that counter number of lower case letters in a file
def loweer():
    s=open("demo.txt")
    lowers=0
    values=s.read()
    for i in values:
        if i.islower():
            lowers+=1
    print("Number of lower case wors in file are ",lowers)            
            
loweer()            

# a function with whic we can write or appen a file from input field
def fieldx():
    a=open("demo.txt","a")
    while True:
        text=input("Enter any text you want to entr in demo File")
        a.write("\n "+ text)
        choice=input("conferm  more or not y/n")
        if choice=="n":
            break
        a.close()

fieldx()
        