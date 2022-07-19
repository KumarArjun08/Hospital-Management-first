import mysql.connector as mycon
from tkinter import *
from sqlconnection import * 

def searchTR_all():
    cur=con.cursor()
    cur.execute("select name,password from Transanctions")
    d=cur.fetchall()
    return d
def searchTR01(x):
    cur = con.cursor()
    cur.execute("select * from Transanctions where Acc_num="+x)

    d=cur.fetchall()
    st=""
    gap="|"
    for i in d:
        st=f"{i[0]:5}{gap}{i[1]:>12}{gap}{i[2]:>20}{gap}{i[3]:>8}{gap}{i[4]:>1}"
    print(st)
    k=StringVar()
    k.set(st)
    print("record updated successfully")
    return st

def searchTR02(x):
    cur = con.cursor()
    cur.execute("select * from Transanctions where Acc_num = %s" %x)

    d=cur.fetchall()
    lis=[]
    liss=[]
    listt=[]
    for i in d:
        st1=""
        gap="|"
        if i[4]=="D":
            st1=f"{i[0]:5}{gap}{i[1]:>18}{gap}{i[2]:>30}{gap}{i[3]:>17}"
            listt.append(st1)
        if i[4]=="P":
            st1=f"{i[0]:5}{gap}{i[1]:>18}{gap}{i[2]:>30}{gap}{i[3]:>17}"
            liss.append(st1)
    lis.append(listt)
    lis.append(liss)
    print(lis)
    print("record updated successfully")
    return lis

def up_paidTR(y):
    cur = con.cursor()
    cur.execute("update Transanctions set status='P' where T_ID=" + y + "")
    con.commit()

    print("record updated successfully")


def up_totalTR(a, b):
    cur = con.cursor()
    cur.execute("update Transanctions set Total_amount=" + b + " where Acc_num=" + a + "")
    con.commit()

    print("record updated successfully")

def up_totalInTR(a,b):
    cur = con.cursor()
    cur.execute("select Fees from employee where D_ID="+str(a))
    d=cur.fetchall()
    cur.execute("update Transanctions set Total_amount=Total_amount+" + str(d[0][0]) + " where Acc_num=" + str(b) + "")
    con.commit()

    print("record updated successfully")

def up_passTR(a, b):
    cur = con.cursor()
    cur.execute("update Transanctions set password='" + b + "' where Acc_no.=" + a + "")
    con.commit()

    print("record updated successfully")


def insert_TR(y, z, k, l):
    cur = con.cursor()
    cur.execute("select T_ID from Transanctions")
    d=cur.fetchall()
    x=1001
    if d!=[]:
        for i in d:
            for j in i:
                if x<j:
                    x=j
        x=x+1

    cur.execute("insert into Transanctions values(%s,%s,%s,%s,%s)", (x, y, z, k, l))
    con.commit()

    print("record updated successfully")

def insert_TR01(y, z, k, l):
    cur = con.cursor()
    cur.execute("select Fees from employee where D_ID="+str(k))
    f=cur.fetchall()
    cur.execute("select T_ID from Transanctions")
    d=cur.fetchall()
    x=1001
    if d!=[]:
        for i in d:
            for j in i:
                if x<j:
                    x=j
        x=x+1

    cur.execute("insert into Transanctions values(%s,%s,%s,%s,%s)", (x, y, z, f[0][0], l))
    con.commit()

    print("record updated successfully")
