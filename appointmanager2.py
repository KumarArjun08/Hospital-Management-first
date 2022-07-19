import csv
import datetime
import tkinter as tk

fn = 'appoint.csv'
dn = 'doctor.csv'
pn = 'patient.csv'
Tn = 'Time_avail.csv'

def writedoc(b):
    l = []
    global dn
    with open(dn, 'a+') as f:
        
        csw = csv.writer(f, lineterminator='\n')
        f.seek(0)
        
        l = list(csv.reader(f))
        if len(l) == 0:
            a = 90001
        else:
            a = int(l[-1][0]) + 1
        rec = [a,b]
        csw.writerow(rec)
    return a

def writepat(b):
    l = []
    global pn
    with open(pn, 'a+') as f:
        
        csw = csv.writer(f, lineterminator='\n')
        f.seek(0)
        
        l = list(csv.reader(f))
        if len(l) == 0:
            a = 10001
        else:
            a = int(l[-1][0]) + 1
        rec = [a,b]
        csw.writerow(rec)
    return a

def write_dcc(k,m,n):
    global Tn
    with open(Tn,'a+') as f:
        csw = csv.writer(f, lineterminator='\n')
        f.seek(0)
        
        l = list(csv.reader(f))
        rec = [k,m,n]
        csw.writerow(rec)
    return l
        
def read_dcc(k,n):
    global Tn 
    with open(Tn,'r') as f:
        l=list(csv.reader(f))
        for i in l:
            if i[0]==k and i[2]==n:
                x=i[1].split(" - ")
                return x
            else:
                return None
