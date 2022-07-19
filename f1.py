from appointmanager2 import *
from tkinter import *
from sqlconnection import *

def new_employee(y, z, k, o, m, l, n):
    a=writedoc(y)
    cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)", (a, y, z, k, o, m, l, n))
    con.commit()
    print("record saved successfully")


def gen(x, y, z):
    s1 = []
    cur.execute("select " + z + " from employee where " + y + "='%s'" % x)
    for l in cur:
        for i in l:
            s1.append(i)
    print(s1)


def select():
    cur.execute("select D_ID,NAME from employee")
    return cur.fetchall()
    

def searche1(x):
    cur = con.cursor()
    cur.execute("select D_ID,Name,salary,feild_of_practice from employee where D_ID="+x)
    d=cur.fetchall()
    st=""
    gap="|"
    for i in d:
        st=f"{i[0]:>5}{gap}{i[1]:>15}{gap}{i[2]:>10}{gap}{i[3]:>15}"
    print(st)
    print("record updated successfully")
    k=StringVar()
    k.set(st)
    return st
    
def searche2(x):
    cur = con.cursor()
    cur.execute("select D_ID,Name,salary,feild_of_practice from employee where name = '%s'" %x)
    d=cur.fetchall()
    l=[]
    for i in d:
        st1=""
        gap="|"
        st1=f"{i[0]:>5}{gap}{i[1]:>15}{gap}{i[2]:>10}{gap}{i[3]:>15}"
        l.append(st1)
        print(st1)
    k=StringVar()
    k.set(st1)
    return l

def searche3(x):
    cur = con.cursor()
    cur.execute("select D_ID,Name,feild_of_practice from employee where name = '%s'" %x)
    d=cur.fetchall()
    st1=""
    l=[]
    for i in d:
        st1=""
        gap="|"
        st1=f"{i[0]:>5}{gap}{i[1]:>15}{gap}{i[2]:>15}"
        l.append(st1)
        print(st1)
    k=StringVar()
    k.set(st1)
    return l

def searche4(x):
    cur = con.cursor()
    cur.execute("select D_ID,Name,feild_of_practice from employee where name like '%"+x+"%'")
    d=cur.fetchall()
    st1=""
    l=[]
    for i in d:
        st1=""
        gap="|"
        st1=f"{i[0]:>5}{gap}{i[1]:>15}{gap}{i[2]:>15}"
        l.append(st1)
        print(st1)
    k=StringVar()
    k.set(st1)
    return l


def up_salary(x, y):
    cur = con.cursor()
    cur.execute("update employee set salary=" + y + " where D_ID=" + str(x))
    con.commit()
    print("record updated successfully")


def up_feild(a, b):
    cur = con.cursor()
    cur.execute("update employee set feild_of_practice ='"+b+"' where D_ID="+str(a))
    con.commit()
    print("record updated successfully")

def check_avail(a,t):
    cur.execute("select ARRIVETime,LEAVETime from employee where D_ID="+a)
    d=cur.fetchall()
    
    if read_dcc(a,t):
        return read_dcc(a,t)
    else:
        return d[0]
    
def invoiceg(a,b):
    cur = con.cursor()
    cur.execute("select Name,Fees from employee where D_ID="+str(a))
    d=cur.fetchall()
    
    l=[]
    for i in d:
        for x in i:
            l.append(x)
            
    cur.execute("select Name from accounts where Acc_Num="+str(b))
    f=cur.fetchall()
    
    for j in f:
        for y in j:
            l.append(y)
    return l



