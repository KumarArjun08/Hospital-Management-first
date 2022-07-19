import mysql.connector as con
from sqlconnection import *

def write(a,b,c,d,e):
    cur.execute("insert into inventory values('"+a+"', '"+b+"', '"+c+"','"+d+"', '"+e+"')")
    con.commit()
    print("records inserted")


def read(q):
    cur.execute("select * from inventory where item_id='"+q+"'")
    print(cur.fetchall())


