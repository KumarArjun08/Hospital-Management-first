import os
def presc_se(ID,Date,I):
    try:
        f=open("Prescripts\\"+ID+"\\"+ID+Date+I+".txt",'r')
        return f.readlines()
    except:
        return []
def presc_wr(ID,Date,I,l):
   try:
        f=open("Prescripts\\"+ID+"\\"+ID+Date+I+".txt","w+")
        f.writelines(l)
        print("added to existing directory")
   except:
        try:
           os.mkdir("Prescripts\\"+ID)
        except:
           os.mkdir("Prescripts")
           os.mkdir("Prescripts\\"+ID)
        f=open("Prescripts\\"+ID+"\\"+ID+Date+I+".txt","w+")
        f.writelines(l)
        print("new directory created and saved")
        


