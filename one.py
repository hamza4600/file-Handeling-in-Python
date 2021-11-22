# we can creat and read delet and appenda data in a file in Pythn i
import os
f=open("demo.txt", "r")
print(f.read())

# readline return only single line of file
q=open("demo.txt", "r")
print(q.readline())

# we can also loop all file
f=open('demo.txt',"r")
for i in f:
    print(i)
    
# os module
# provide current directory of file
print(os.getcwd())
# change current directory chdir() 
# we have move to that file 
print(os.chdir("/home/hamza/Desktop/PythonPractice"))
# lsit file and folders in a folder listdir()


# we can also access the files from the other dirctorie and folders


# current folder path

a=os.getcwd()

print(a)

# move to differtn files

print(os.chdir("/home/hamza/Desktop/PythonPractice"))



print(os.uname())

print(os.ctermid())

print(os.stat("one.py"))

os.system("firefox")

