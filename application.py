#1)run the installation module first
#2)change the sql password at the sqlconnection

from time import *

#The Driver Code

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("=====================Welcome to the Hospital Management=======================")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
sleep(0.5)

from GUI1 import *

#checking the required packages

sleep(0.5)
print("intialising...")

sleep(0.5)
print("checking required packages")

cur.execute("show tables")
x=cur.fetchall()

for i in x:
    for k in i:
        sleep(0.5)
        print("checking structure:--"+k)
        if k in ("accounts","employee","pharmacy","transanctions"):
            sleep(0.1)
            print("sucessful!")
        else:
            sleep(0.1)
            print("error in loading \n please run the installion module")
            sleep(0.2)
            quit()

#calling the start function

sleep(0.1)
print("launching the application...")
sleep(1)
lgn_disp1()
