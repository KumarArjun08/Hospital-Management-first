from appointmanager1 import *
from tkinter import *
from f1 import *
from f3 import *
from f2 import *
from f4 import *
from f5 import *
from PIL import ImageTk, Image
from tkinter import messagebox
import tkinter.font as TkFont
from timemanager import *
from Acc_Link import *
from datetime import *
from prescript import *

def new_ac():
        window8 = Tk()
        window8.title("accounts")

        lb1x0 = Label(window8, text="new account",font=("Arial Bold",15))
        lb1x0.grid(column=0, row=0)
        
        lb1x1 = Label(window8, text="name")
        lb1x1.grid(column=0, row=4)

        lb1x2 = Label(window8, text="ammount due")
        lb1x2.grid(column=0, row=6)

        lb1x3 = Label(window8, text="amount paid")
        lb1x3.grid(column=0, row=8)

        txtx1 = Entry(window8, width=30)
        txtx1.grid(column=2, row=4)

        txtx2 = Entry(window8, width=30)
        txtx2.grid(column=2, row=6)

        txtx3 = Entry(window8, width=30)
        txtx3.grid(column=2, row=8)
        
        txtx1.insert(0, "name")
        txtx2.insert(0, "10000")
        txtx3.insert(0, "10000")

        def ins_ac():
                insert_acc(txtx1.get(),int(txtx3.get()),int(txtx2.get()))
                writepat(txtx1.get())
                insert_TR(convert(txtx1.get())[0][0],"ADMISSION","10000","D")
        bx = Button(window8, text="submit", width=15, command=ins_ac)
        bx.grid(column=2, row=10)

        window8.geometry('320x200')
        window8.mainloop()

def new_empl():
        window9 = Tk()
        window9.title("employee")

        lab1x0 = Label(window9, text="new employee",font=("Arial Bold",15))
        lab1x0.grid(column=0, row=0)
        
        lab1x1 = Label(window9, text="name")
        lab1x1.grid(column=0, row=4)

        lab1x2 = Label(window9, text="medical lisc")
        lab1x2.grid(column=0, row=6)

        lab1x3 = Label(window9, text="Arrival at clinic")
        lab1x3.grid(column=0, row=8)

        lab1x4 = Label(window9, text="Leave from clinic")
        lab1x4.grid(column=0, row=9)

        lab1x01 = Label(window9, text="Fees consult")
        lab1x01.grid(column=0, row=10)

        lab1x02 = Label(window9, text="salary")
        lab1x02.grid(column=0, row=12)

        lab1x03 = Label(window9, text="feild of study")
        lab1x03.grid(column=0, row=14)

        textx1 = Entry(window9, width=30)
        textx1.grid(column=2, row=4)

        textx2 = Entry(window9, width=30)
        textx2.grid(column=2, row=6)

        textx3 = Entry(window9, width=30)
        textx3.grid(column=2, row=8)

        textx4 = Entry(window9, width=30)
        textx4.grid(column=2, row=9)

        textx01 = Entry(window9, width=30)
        textx01.grid(column=2, row=10)

        textx02 = Entry(window9, width=30)
        textx02.grid(column=2, row=12)

        textx03 = Entry(window9, width=30)
        textx03.grid(column=2, row=14)

        textx1.insert(0, "name")
        textx2.insert(0, "A0123456xx")
        textx3.insert(0, "HH:mm")
        textx4.insert(0, "HH:mm")

        textx01.insert(0, "1000")
        textx02.insert(0, "100000")
        textx03.insert(0, "feild")

        bex = Button(window9, text="submit", width=15, command=lambda: new_employee(textx1.get(),textx2.get(),textx3.get(),textx4.get(),int(textx01.get()),float(textx02.get()),textx03.get()))
        bex.grid(column=2, row=16)

        window9.geometry('450x300')
        window9.mainloop()        

def appointde():
    windowx2 = Toplevel()
    windowx2.title("appointments")

    image4=ImageTk.PhotoImage(Image.open('dispp.png'))

    lbx5=Canvas(windowx2,width=920,height=600,bg="white")
    lbx5.create_image(0, 0 ,anchor=NW,image=image4)
    lbx5.grid(column=0,row=0)
    lbx5.grid_propagate(0)

    lbx18 = Label(lbx5, text="select the appointment", font=("Arial Bold", 15))
    lbx18.grid(column=2, row=2)

    lbx19 = Label(lbx5, text="Appointments...", font=("Segoe Print", 20))
    lbx19.grid(column=2, row=0)

    txtx13 = Entry(lbx5, width=30)
    txtx13.grid(column=2, row=4)
    
    lbx20 = Label(lbx5, text="appointment id")
    lbx20.grid(column=1, row=4)

    def choosex():
        deletea(int(txtx13.get()))

    bx5 = Button(lbx5, text="delete",command=choosex)
    bx5.grid(column=2, row=6)

    windowx2.geometry('400x200')
    windowx2.mainloop()

    
def appointse():
    windowx3 = Toplevel()
    windowx3.title("appointments")
    my_font=TkFont.Font(windowx3,family="Monaco",size=10)

    image4=ImageTk.PhotoImage(Image.open('dispp.png'))

    lbk5=Canvas(windowx3,width=920,height=600,bg="white")
    lbk5.create_image(0, 0 ,anchor=NW,image=image4)
    lbk5.grid(column=0,row=0)
    lbk5.grid_propagate(0)    

    lbx318 = Label(lbk5, text="select the appointment", font=("Arial Bold", 15))
    lbx318.grid(column=2, row=2)

    lbx319 = Label(lbk5, text="Appointments...", font=("Segoe Print", 20))
    lbx319.grid(column=2, row=0)

    txtx313 = Entry(lbk5, width=30)
    txtx313.grid(column=2, row=4)
    
    lbx320 = Label(lbk5, text="patient id")
    lbx320.grid(column=1, row=4)

    framea=LabelFrame(lbk5,width=350,height=50)
    framea.grid(column=2,row=18)
    scrolla=Scrollbar(framea,orient=VERTICAL)
    listba=Listbox(framea,height=5,width=55,font=my_font,yscrollcommand=scrolla.set)
    scrolla.config(command=listba.yview)
    scrolla.pack(side=RIGHT,fill=Y)
    listba.pack()
    gap=" | "
    lo=["Name","Doctor","Date","Time"]
    listba.insert(END,f"{lo[0]:>10}{gap}{lo[1]:>10}{gap}{lo[2]:>10}{gap}{lo[3]:>13}")
    listba.insert(END,'----------------------------------------------------------')
    
    def choosex3():
        l=searcha(txtx313.get())
        listba.insert(END,l)
    def clearap():
        listba.delete(2,END)

    bx35 = Button(lbk5, text="search",command=choosex3,width=15)
    bx35.grid(column=2, row=6,pady=5)
    box35 = Button(lbk5, text="clear",command=clearap,width=15)
    box35.grid(column=2, row=19,pady=5)

    windowx3.geometry('540x300')
    windowx3.mainloop()

def appointup():
    windowx4 = Toplevel()
    windowx4.title("appointments")

    lbx418 = Label(windowx4, text="select the appointment", font=("Arial Bold", 15))
    lbx418.grid(column=2, row=2)
    lbx419 = Label(windowx4, text="Appointments...", font=("Segoe Print", 20))
    lbx419.grid(column=2, row=0)
    lbx420 = Label(windowx4, text="ID")
    lbx420.grid(column=1, row=4)

    txtx414 = Entry(windowx4, width=30)
    txtx414.grid(column=2, row=4)

    txtx413 = Entry(windowx4, width=30)
    txtx413.grid(column=2, row=6)

    clickx41 = StringVar(windowx4)
    clickx41.set("time")

    dropx4 = OptionMenu(windowx4, clickx41, "time", "status", "date")
    dropx4.config(width=7)
    dropx4.grid(column=1, row=6)

    def choosex4():
        updatea(int(txtx414.get()),clickx41.get(),txtx413.get())

    bx45 = Button(windowx4, text="update",command=choosex4)
    bx45.grid(column=2, row=8)

    windowx4.geometry('350x250')
    windowx4.mainloop()

def invoice(a,b,c,d,e):
    res=Toplevel()
    res.title("Record")
    
    la=Label(res,text="Appointment Summary",font=("Arial Bold",15))
    la.grid(column=0,row=0,columnspan=2)
    
    la1=Label(res,text="Name:--",font=("Arial Bold",10))
    la1.grid(column=0,row=1)

    la2=Label(res,text="Doctor:--",font=("Arial Bold",10))
    la2.grid(column=0,row=2)

    la3=Label(res,text="Time:--",font=("Arial Bold",10))
    la3.grid(column=0,row=3)

    la4=Label(res,text="Date:--",font=("Arial Bold",10))
    la4.grid(column=0,row=4)

    la5=Label(res,text="Price:--",font=("Arial Bold",10))
    la5.grid(column=0,row=5)

    la6=Label(res,text=a)
    la6.grid(column=1,row=1)

    la7=Label(res,text=b)
    la7.grid(column=1,row=2)

    la8=Label(res,text=c)
    la8.grid(column=1,row=3)

    la9=Label(res,text=d)
    la9.grid(column=1,row=4)

    la10=Label(res,text=e)
    la10.grid(column=1,row=5)

    res.geometry("250x150")
    res.mainloop()
    
def appointcr():
    window6 = Toplevel()
    window6.title("appointments")

    image4=ImageTk.PhotoImage(Image.open('dispp.png'))

    lbn5=Canvas(window6,width=920,height=600,bg="white")
    lbn5.create_image(0, 0 ,anchor=NW,image=image4)
    lbn5.grid(column=0,row=0)
    lbn5.grid_propagate(0)

    my_font=TkFont.Font(window6,family="Monaco",size=10)

    lb18 = Label(lbn5, text="select the appointment", font=("Arial Bold", 15))
    lb18.grid(column=2, row=2)

    lb19 = Label(lbn5, text="Appointments...", font=("Segoe Print", 20))
    lb19.grid(column=2, row=0)

    txt13 = Entry(lbn5, width=30)
    txt13.grid(column=2, row=4)

    txt14 = Entry(lbn5, width=30)
    txt14.grid(column=2, row=6)

    txt30 = Entry(lbn5, width=30)
    txt30.grid(column=2, row=10)

    txt31 = Entry(lbn5, width=30)
    txt31.grid(column=2, row=12)

    lb20 = Label(lbn5, text="Doctor ID")
    lb20.grid(column=1, row=4)

    lb21 = Label(lbn5, text="Patient ID")
    lb21.grid(column=1, row=6)

    lb31 = Label(lbn5, text="enter the date")
    lb31.grid(column=1, row=10)

    lb32 = Label(lbn5, text="status")
    lb32.grid(column=1, row=12)

    lb33 = Label(lbn5, text="time")
    lb33.grid(column=1, row=16)

    frama=LabelFrame(lbn5,width=350,height=50)
    frama.grid(column=2,row=16)
    
    scrollap=Scrollbar(frama,orient=VERTICAL)
    listbap=Listbox(frama,height=5,width=25,font=my_font,yscrollcommand=scrollap.set)
    
    scrollap.config(command=listbap.yview)
    scrollap.pack(side=RIGHT,fill=Y)
    listbap.pack()
    
    gap="|"
    loap=["acno.","name","due","paid"]
    listbap.insert(END,'------------------------------------------------')
    
    def choose():
        listbap.delete(1,END)
        d=check_avail(txt13.get(),txt30.get())
        k=appoint_time(txt30.get(),txt13.get(),d[0],d[1])
        for i in k:
                listbap.insert(END,i)
                
    def time_sel():
        x=listbap.get(ANCHOR)
        listbap.delete(ANCHOR)
        
        writea(txt14.get(),txt13.get(),x,txt30.get(),txt31.get())
        up_totalIn(int(txt13.get()),int(txt14.get()))
        
        insert_TR01(txt14.get(),"APPOINTMENT",txt13.get(),"D")
        l=invoiceg(int(txt13.get()),int(txt14.get()))
        
        invoice(l[2],l[0],x,txt30.get(),l[1])
        
    b5 = Button(lbn5, text="search time",command=choose,width=10)
    b5.grid(column=2, row=14,pady=5)
    
    bsel = Button(lbn5, text="Create",command=time_sel,width=10)
    bsel.grid(column=2, row=18,pady=5)

    window6.geometry('400x330')
    window6.mainloop()

def linkL(a):
    wind=Tk()
    wind.title("LINK")
    lblink0=Label(wind,text="LINK>>>",font=("Arial Bold",15))
    lblink0.grid(column=0,row=0)
    
    lblink1=Label(wind,text="Enter link name")
    lblink1.grid(column=0,row=4)
    
    txtlin1 = Entry(wind, width=30)
    txtlin1.grid(column=2, row=4)

    def my_Link():
            writeLink(a,txtlin1.get())

    blin = Button(wind, text="Link",command=my_Link,width=10)
    blin.grid(column=2, row=6,pady=5)
    
    wind.geometry('290x125')
    wind.mainloop()

def prescripwr(I,ID):
    root=Toplevel()
    root.title("prescription")
    
    m=str(datetime.now())[:10].split("-")

    DATE=""
    DATE=m[2]+"-"+m[1]+"-"+m[0]

    txttt=Text(root,height=35,width=80)
    txttt.grid(row=0,column=0)
    txttt.insert(END,"Date:- "+DATE+"\n")
    txttt.insert(END,"ID:- "+ID+"\n")
    txttt.insert(END,"Doctor:- "+I+"\n")

    def write_prescript(ID,DATE,I):
        presc_wr(ID,DATE,I,txttt.get(1.0,END))
            
        
    bt=Button(root,text="Submit",command=lambda: write_prescript(ID,DATE,I),width=10)
    bt.grid(row=1,column=0)

    root.geometry('630x601')
    root.mainloop()

def prescripop(I,ID,date):
    root1=Toplevel()
    root1.title("prescription")
    
    m=str(datetime.now())[:10].split("-")

    DATE=""
    DATE=m[2]+"-"+m[1]+"-"+m[0]

    txttt=Text(root1,height=35,width=80)
    txttt.grid(row=0,column=0)
    l=presc_se(ID,date,I)
    for i in l:
        txttt.insert(END,i)
    def save_prescript(ID,date,I):
        presc_wr(ID,DATE,I,txttt.get(1.0,END))
        
    bt=Button(root1,text="Save",command=lambda: save_prescript(ID,date,I),width=10)
    bt.grid(row=1,column=0)

    root1.geometry('630x601')
    root1.mainloop()
        
def prescrip_open_pat(I,ID,date):
    root1=Toplevel()
    root1.title("prescription")
    
    m=str(datetime.now())[:10].split("-")

    DATE=""
    DATE=m[2]+"-"+m[1]+"-"+m[0]

    txttt=Text(root1,height=35,width=80)
    txttt.grid(row=0,column=0)
    l=presc_se(ID,date,I)
    for i in l:
        txttt.insert(END,i)
    def save_prescript(ID,date,I):
        presc_wr(ID,DATE,I,txttt.get(1.0,END))
        
    bt=Button(root1,text="Save",command=lambda: save_prescript(ID,date,I),width=10)
    #bt.grid(row=1,column=0)

    root1.geometry('630x601')
    root1.mainloop()

