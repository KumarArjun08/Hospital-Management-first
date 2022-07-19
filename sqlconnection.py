import mysql.connector as mycon


try:
    con=mycon.connect(host="localhost",username="root",passwd="Br13s8010",database="hospital_m")
    if con.is_connected():
        print("connection successful")
    cur=con.cursor()


except mycon.errors.ProgrammingError:
    print("wrong sql passwd plz change it in application file")
    quit()

