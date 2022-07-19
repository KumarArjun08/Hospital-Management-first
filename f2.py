import mysql.connector as mycon
from tkinter import *
from sqlconnection import *

def searchp1(x):
    cur = con.cursor()
    cur.execute("select * from pharmacy where Drug_ID='%s'" %x)

    d=cur.fetchall()
    l=[]
    gap="|"
    for i in d:
        st=""
        st=f"{i[0]:>5}{gap}{i[1]:>30}{gap}{i[2]:>10}"
        l.append(st)
    print(st)
    k=StringVar()
    k.set(st)

    print("record updated successfully")
    return l
    
def searchp2(x):
    cur = con.cursor()
    print()
    cur.execute("select * from pharmacy where name like '"+x+"%'")
    gap="|"
    d=cur.fetchall()
    l=[]
    for i in d:
        st=""
        st=f"{i[0]:>5}{gap}{i[1]:>30}{gap}{i[2]:>10}"
        l.append(st)
    print(st)
    k=StringVar()
    k.set(st)

    print("record updated successfully")
    return l

def sel():
    cur.execute("select * from pharmacy")
    return cur.fetchall()

def ins(a, b, c, d, e, f):
    cur.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s)",(a, b, c, d, e, f))
    con.commit()
    print("record inserted successfully")

def red_qua(a,b):
    cur.execute("update pharmacy set Quantity=Quantity-" + str(b) + " where Drug_Id =" + str(a))
    con.commit()
    print("record updated successfully")

