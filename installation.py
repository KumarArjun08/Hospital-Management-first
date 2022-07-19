#installation module
#Run This before you start working on the Application

import mysql.connector as mycon
from tkinter import *
password=input("enter your sql passwd")

con = mycon.connect(host="localhost", user="root", passwd=password)

if con.is_connected():
    print("connection successful")
cur = con.cursor()

f=open("empl.txt",'r')
x=f.readlines()

for i in x:
    cur.execute(i)
print("employee structure successfully created")

f.close()

f1=open("AccTable.txt",'r')
x1=f1.readlines()

for i in x1:
    cur.execute(i)
print("accounts structure suceessfully created")

f1.close()

f2=open("pharmtable.txt",'r')
x2=f2.readlines()

for i in x2:
    cur.execute(i)
    con.commit()
print("pharmacy structure suceesfully created")

f2.close()

f4=open("Transanc.txt",'r')
x4=f4.readlines()

for i in x4:
    cur.execute(i)
print("transanction structure suceessfully created")

f4.close()

cur.close()
con.close()

print("installation complete")
