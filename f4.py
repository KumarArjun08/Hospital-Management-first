import mysql.connector as mycon
from tkinter import *
from sqlconnection import * 

def search_all():
    cur=con.cursor()
    cur.execute("select name,password from accounts")
    d=cur.fetchall()
    return d
def search01(x):
    cur = con.cursor()
    cur.execute("select * from accounts where Acc_num="+x)

    d=cur.fetchall()
    st=""
    gap="|"
    for i in d:
        st=f"{i[0]:5}{gap}{i[1]:>12}{gap}{i[2]:>8}{gap}{i[3]:>8}"
    print(st)
    k=StringVar()
    k.set(st)
    print("record updated successfully")
    return st
def convert(t):
    cur=con.cursor()
    cur.execute("select Acc_num from accounts where name='"+t+"'")
    d=cur.fetchall()
    return d

def search02(x):
    cur = con.cursor()
    cur.execute("select * from accounts where name = '%s'" %x)

    d=cur.fetchall()
    lis=[]
    for i in d:
        st1=""
        gap="|"
        st1=f"{i[0]:5}{gap}{i[1]:>12}{gap}{i[2]:>8}{gap}{i[3]:>8}"
        lis.append(st1)

    print(lis)
    print("record updated successfully")
    return lis

def up_paid(x, y):
    cur = con.cursor()
    cur.execute("update accounts set Amount_paid=" + y + " where Acc_num=" + x + "")
    con.commit()

    print("record updated successfully")


def up_total(a, b):
    cur = con.cursor()
    cur.execute("update accounts set Total_amount=" + b + " where Acc_num=" + a + "")
    con.commit()

    print("record updated successfully")

def up_totalIn(a,b):
    cur = con.cursor()
    cur.execute("select Fees from employee where D_ID="+str(a))
    d=cur.fetchall()
    cur.execute("update accounts set Total_amount=Total_amount+" + str(d[0][0]) + " where Acc_num=" + str(b) + "")
    con.commit()

    print("record updated successfully")
    
def up_paidIn(a,b):
    cur.execute("update accounts set Amount_Paid=Amount_Paid+" + str(a) + " where Acc_num=" + str(b) + "")
    con.commit()

    print("record updated successfully")

def up_pass(a, b):
    cur = con.cursor()
    cur.execute("update accounts set password='" + b + "' where Acc_no.=" + a + "")
    con.commit()

    print("record updated successfully")


def insert_acc(y, z, k):
    cur = con.cursor()
    cur.execute("select acc_num from accounts")
    d=cur.fetchall()
    x=10001
    if d!=[]:
        for i in d:
            for j in i:
                if x<j:
                    x=j
        x=x+1

    cur.execute("insert into accounts values(%s,%s,%s,%s,%s)", (x, y, z, k, x))
    con.commit()

    print("record updated successfully")
