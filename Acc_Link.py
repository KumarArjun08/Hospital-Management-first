import csv
import datetime
import tkinter as tk

#Linking several accounts so that we can display them together on patients window

#Creating a csv file as a storage method
fn = 'Link.csv'


#writing into the csv
def writeLink(b,c):
    l = []
    global fn
    with open(fn, 'a+') as f:
        
        csw = csv.writer(f, lineterminator='\n')
        f.seek(0)
        l = list(csv.reader(f))
        new=[]
        for i in l:
            if i[0]==b:
                deleteLink(b)
                new=i
                new.append(c)
                
        if new==[]:
            new=[b,c]
        csw.writerow(new)
        print("acc linked")

#deleting a record from the csv
def deleteLink(ID):
    global fn
    with open(fn, 'r') as f:
        flag = False
        csr = csv.reader(f)
        reclst = list(csr)
        for i in range(len(reclst)):
            if reclst[i][0]==ID:
                flag = True
                reclst.pop(i)
                break
    with open(fn, 'w') as f:
        csw = csv.writer(f, lineterminator='\n')
        csw.writerows(reclst)

    if flag:
        print('Record deleted')
    else:
        print('Record not found')

#Searching a link        
def searchLink(a):
    l = []
    global fn
    with open(fn, 'a+') as f:
        
        csw = csv.writer(f, lineterminator='\n')
        f.seek(0)
        l = list(csv.reader(f))
        for i in l:
           if i[0]==a:
               return i
