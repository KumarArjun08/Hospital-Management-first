from appointmanager1 import *
from appointmanager2 import *
from tkinter import *
from f1 import *
from f3 import *
from f2 import *
from f4 import *
from f5 import *
from PIL import ImageTk, Image
from tkinter import messagebox
from GUI3 import *
import tkinter.font as TkFont
from Acc_Link import *

def acc():
    window3 = Toplevel()
    window3.title("accounts")
    
    image4=ImageTk.PhotoImage(Image.open('bg.png'))

    lbc5=Canvas(window3,width=920,height=600,bg="white")
    lbc5.create_image(0, 0 ,anchor=NW,image=image4)
    lbc5.grid(column=0,row=0)
    lbc5.grid_propagate(0)

    my_font=TkFont.Font(window3,family="Monaco",size=10)
    
    framea2=LabelFrame(lbc5,width=440,height=290)
    framea2.config(bg="white")
    framea2.grid(column=2,row=2,padx=20,pady=20)
    framea2.grid_propagate(0)
    
    framea3=LabelFrame(lbc5,width=350,height=290)
    framea3.grid(column=3,row=2)
    framea3.config(bg="white")
    framea3.grid_propagate(0)

    image3=ImageTk.PhotoImage(Image.open('images01.png'))
    
    lbc3=Canvas(framea2,width=500,height=400,bg="white")
    lbc3.create_image(0, 0 ,anchor=NW,image=image3)
    lbc3.grid(column=0,row=0)
    lbc3.grid_propagate(0)

     
    lbc4=Canvas(framea3,width=400,height=400,bg="white")
    
    lbc4.create_image(0, 0 ,anchor=NW,image=image3)
    lbc4.grid(column=0,row=0)
    lbc4.grid_propagate(0)


    lb3 = Label(lbc3, text="select the account", font=("Arial Bold", 15),bg="white")
    lb3.grid(column=2, row=2)

    lba3 = Label(lbc4, text="updating account", font=("Arial Bold", 15),bg="white")
    lba3.grid(column=2, row=2)

    lb4 = Label(lbc5, text="Accounts Department", font=("Segoe Print", 25),bg="snow")
    lb4.grid(column=2, row=0,columnspan=3)


    txt4 = Entry(lbc3, width=30)
    txt4.grid(column=2, row=4)

    txt5 = Entry(lbc3, width=30)
    txt5.grid(column=2, row=6,padx=3,pady=3)

    txt6 = Entry(lbc4, width=30)
    txt6.grid(column=2, row=12, padx=5, pady=5)

    teexta = Entry(lbc4, width=30)
    teexta.grid(column=2, row=4)

    lb5 = Label(lbc3, text="account no.",bg="white")
    lb5.grid(column=1, row=4)

    lba = Label(lbc4, text="account no.",bg="white")
    lba.grid(column=1, row=4,padx=5,pady=5)


    click1 = StringVar(window3)
    click1.set("col. value")

    drop1 = OptionMenu(lbc4, click1,"acc_due", "acc_paid")
    drop1.config(width=10)
    drop1.grid(column=1, row=12)

    lbx = Label(lbc3, text="new account ??", font=("Arial Bold", 10),bg="white")
    lbx.grid(column=1, row=22)

    lb6 = Label(lbc3, text="name search",bg="white")
    lb6.grid(column=1, row=6)

    lb7 = Label(lbc4, text="enter the value to update", font=("Arial Bold", 10),bg="white")
    lb7.grid(column=2, row=10)

    lbf1 = Label(lbc3, text="search results:-", font=("Arial Bold", 10),bg="white")
    lbf1.grid(column=1, row=18)

    frame=LabelFrame(lbc3,width=350,height=50)
    frame.grid(column=2,row=18)
    
    scroll=Scrollbar(frame,orient=VERTICAL)
    listb=Listbox(frame,height=5,width=38,font=my_font,yscrollcommand=scroll.set)
    
    scroll.config(command=listb.yview)
    scroll.pack(side=RIGHT,fill=Y)
    listb.pack()
    
    gap="|"
    lo=["acno.","name","Paid","Due"]
    listb.insert(END,f"{lo[0]:5}{gap}{lo[1]:>12}{gap}{lo[2]:>8}{gap}{lo[3]:>8}")
    listb.insert(END,'------------------------------------------------')
    
    def search1():
        nonlocal listb
        if txt4.get()!="":
            l=search01(txt4.get())
            listb.insert(END,l)
        elif txt5.get()!="":
            l=search02(txt5.get())
            for i in l:
                listb.insert(END,i)
                
    def update01():
        if click1.get()=="acc_due":
            up_total(teexta.get(),txt6.get())
        if click1.get()=="acc_paid":
            up_paid(teexta.get(),txt6.get())
    def clear():
        listb.delete(2,END)
    
    b1 = Button(lbc3, text="select",command=search1, width=15)
    b1.grid(column=2, row=8,padx=10,pady=10)

    bu1 = Button(lbc4, text="update(acc_no. only)",command=update01, width=15)
    bu1.grid(column=2, row=16)

    by = Button(lbc3, text="sign in", command=new_ac, width=15)
    by.grid(column=2, row=22)

    bcl = Button(lbc3, text="Clear", command=clear, width=15)
    bcl.grid(column=2, row=20,pady=5)
    
    window3.config(bg="white")
    window3.geometry('845x390')
    window3.mainloop()


def pharm():
    window4 = Toplevel()
    window4.title("pharmacy")

    my_font=TkFont.Font(window4,family="Monaco",size=10)

    image4=ImageTk.PhotoImage(Image.open('newph.png'))
    
    lbc6=Canvas(window4,width=600,height=600,bg="white")
    lbc6.create_image(0, 0 ,anchor=NW,image=image4)
    lbc6.grid(column=0,row=0)
    lbc6.grid_propagate(0)


    lba8 = Label(lbc6, text="Pharmacy database", font=("Arial Bold", 15),bg="white")
    lba8.grid(column=2, row=2)

    lb8 = Label(lbc6, text="Pharmacy Logs directory", font=("Segoe Print", 20),bg="white")
    lb8.grid(column=2, row=0)

    txt7 = Entry(lbc6, width=30)
    txt7.grid(column=2, row=4)

    txt8 = Entry(lbc6, width=30)
    txt8.grid(column=2, row=6)

    txt9 = Entry(lbc6, width=30)
    txt9.grid(column=2, row=10, padx=5, pady=5)

    lb9 = Label(lbc6, text="item identity no.",bg="white")
    lb9.grid(column=1, row=4)

    click2 = StringVar(lbc6)
    click2.set("Quantity")

    drop2 = OptionMenu(lbc6, click2,"1","2","3","4","5","6","7","8")
    drop2.config(width=7)
    drop2.grid(column=1, row=10)

    lb10 = Label(lbc6, text="name search",bg="white")
    lb10.grid(column=1, row=6)

    lb11 = Label(lbc6, text="Enter the Acc. no.", font=("Arial Bold", 10),bg="white")
    lb11.grid(column=2, row=9)

    lbf1 = Label(lbc6, text="search results:-", font=("Arial Bold", 10),bg="white")
    lbf1.grid(column=1, row=7)

    lbf = Label(lbc6)
    lbf.grid(column=2, row=13)

    frameph=LabelFrame(lbc6,width=350,height=50)
    frameph.grid(column=2,row=7)
    
    scrollph=Scrollbar(frameph,orient=VERTICAL)
    listbph=Listbox(frameph,height=5,width=50,font=my_font,yscrollcommand=scrollph.set)
    
    scrollph.config(command=listbph.yview)
    scrollph.pack(side=RIGHT,fill=Y)
    listbph.pack()
    
    gap="|"
    lo=["ID","Name","Price"]
    listbph.insert(END,f"{lo[0]:>5}{gap}{lo[1]:>30}{gap}{lo[2]:>10}")
    listbph.insert(END,'--------------------------------------------------------------')


    def searchp():
        nonlocal listbph
        if txt7.get()!="":
            l=searchp1(txt7.get())
            for i in l:
                listbph.insert(END,i)
            
        elif txt8.get()!="":
            l=searchp2(txt8.get())
            for i in l:
                listbph.insert(END,i)
    def BILLP():
        l=listbph.get(ANCHOR)
        newl=l.split("|")
        red_qua(newl[0].lstrip,click2.get())
        insert_TR(int(txt9.get()),newl[1].lstrip(),int(newl[2].lstrip()),"D")
        
    def newmed():
        pass

    b2 = Button(lbc6, text="Search",command=searchp,width=15)
    b2.grid(column=2, row=8)

    b3 = Button(lbc6, text="Add to Acc",command=BILLP,width=15)
    b3.grid(column=2, row=13,pady=7)

    b4 = Button(lbc6, text="New Med",command=newmed,width=15)
    b4.grid(column=2, row=16,pady=7)

    window4.geometry('600x400')
    window4.mainloop()


def empl():
    window5 = Toplevel()
    window5.title("employee data")
    
    my_font=TkFont.Font(window5,family="Monaco",size=10)
    
    framee2=LabelFrame(window5,width=550,height=310)
    framee2.grid(column=2,row=2,padx=20,pady=20)
    framee2.grid_propagate(0)
    
    framee3=LabelFrame(window5,width=400,height=310)
    framee3.grid(column=3,row=2)
    framee3.grid_propagate(0)

    lb12 = Label(framee2, text="select the employee", font=("Arial Bold", 15))
    lb12.grid(column=2, row=2)

    lb13 = Label(window5, text="Employees Data..", font=("Segoe Print", 25))
    lb13.grid(column=2, row=0,columnspan=3)

    lbe13 = Label(framee3, text="Update Record", font=("Arial Bold", 15))
    lbe13.grid(column=2, row=4)

    txt10 = Entry(framee2, width=30)
    txt10.grid(column=2, row=4)

    txt11 = Entry(framee2, width=30)
    txt11.grid(column=2, row=6)

    txt12 = Entry(framee3, width=30)
    txt12.grid(column=2, row=12)

    txte12 = Entry(framee3, width=30)
    txte12.grid(column=2, row=8)

    lb14 = Label(framee2, text="doctor ID")
    lb14.grid(column=0, row=4)

    click3 = StringVar(window5)
    click3.set("column")

    drop3 = OptionMenu(framee3, click3,"salary","department")
    drop3.config(width=10)
    drop3.grid(column=0, row=12)

    lb15 = Label(framee2, text="Name Search")
    lb15.grid(column=0, row=6)

    lbe15 = Label(framee3, text="Doctor Id")
    lbe15.grid(column=0, row=8)

    lb16 = Label(framee3, text="enter the value", font=("Arial Bold", 10))
    lb16.grid(column=2, row=10)

    lb17 = Label(framee2, text="new employee ??", font=("Arial Bold", 10))
    lb17.grid(column=2, row=20)

    lbf1 = Label(framee2, text="search results:-", font=("Arial Bold", 10))
    lbf1.grid(column=0, row=18)

    lbf = Label(framee2)
    lbf.grid(column=2, row=21)

    framee=LabelFrame(framee2,width=300,height=50)
    framee.grid(column=2,row=18)
    
    scrolle=Scrollbar(framee,orient=VERTICAL)
    listbe=Listbox(framee,height=5,width=52,font=my_font,yscrollcommand=scrolle.set)
    
    scrolle.config(command=listbe.yview)
    scrolle.pack(side=RIGHT,fill=Y)
    listbe.pack()
    
    gap="|"
    le=["Dc_Id","Name","Salary","Department"]
    listbe.insert(END,f"{le[0]:5}{gap}{le[1]:>15}{gap}{le[2]:>10}{gap}{le[3]:>15}")
    listbe.insert(END,'------------------------------------------------')
    
    def searche():
        nonlocal listbe
        if txt10.get()!="":
            l=searche1(txt10.get())
            listbe.insert(END,l)
        elif txt11.get()!="":
            l=searche2(txt11.get())
            for i in l:
                listbe.insert(END,i)
                
    def update02():
        if click3.get()=="department":
            up_feild(int(txte12.get()),txt12.get())
        if click3.get()=="salary":
            up_salary(int(txte12.get()),txt12.get())

    def cleare():
        listbe.delete(2,END)
            

    b3 = Button(framee2, text="select",command=searche,width=15)
    b3.grid(column=2, row=8,pady=10)

    bu2 = Button(framee3, text="update(acc no.)",command=update02, width=15)
    bu2.grid(column=2, row=14)

    b4 = Button(framee2, text="sign in",command=new_empl,width=15)
    b4.grid(column=2, row=21,pady=10)

    bcle = Button(framee2, text="Clear", command=cleare, width=15)
    bcle.grid(column=2, row=19,pady=5)

    window5.geometry('1000x400')
    window5.mainloop()

def pre_appoint():
    windowx1 = Toplevel()
    windowx1.title("appointment")

    image4=ImageTk.PhotoImage(Image.open('dispp.png'))

    lbo5=Canvas(windowx1,width=920,height=600,bg="white")
    lbo5.create_image(0, 0 ,anchor=NW,image=image4)
    lbo5.grid(column=0,row=0)
    lbo5.grid_propagate(0)

    lbx3 = Label(lbo5, text="enter your requirement", font=("Arial Bold", 10))
    lbx3.grid(column=0, row=2)

    lbx4 = Label(lbo5, text="The Appointment Manager", font=("Segoe Print", 15))
    lbx4.grid(column=0, row=0)

    clickx1 = StringVar(windowx1)
    clickx1.set("Create")

    dropx = OptionMenu(lbo5, clickx1, "Create", "Search", "Delete", "Update")
    dropx.config(width=11)
    dropx.grid(column=1, row=2)

    def selectx1():
        if clickx1.get() == "Create":
            appointcr()
        if clickx1.get() == "Delete":
            appointde()
        if clickx1.get() == "Search":
            appointse()
        if clickx1.get() == "Update":
            appointup()
        
    bx1 = Button(lbo5, text="Select", command=selectx1,width=14)
    bx1.grid(column=1, row=4)

    windowx1.geometry('420x150')
    windowx1.mainloop()

def patient(nam,ID):
    window7 = Toplevel()
    window7.title("patient")

    my_font=TkFont.Font(window7,family="Monaco",size=10)

    framep1=LabelFrame(window7,width=500,height=250,padx=5,pady=5,bg='white')
    framep1.grid(column=0,row=2,padx=10,pady=10)
    framep1.grid_propagate(0)

    lbp1 = Label(window7, text=" ",bg='white')
    lbp1.grid(column=1, row=2)

    framep2=LabelFrame(window7,width=500,height=250,bg='white')
    framep2.grid(column=2,row=2)

    framep3=LabelFrame(window7,width=500,height=250,bg='white')
    framep3.grid(column=0,row=4)

    framep4=LabelFrame(window7,width=500,height=250,bg='white')
    framep4.grid(column=2,row=4)

    framep2.grid_propagate(0)
    framep3.grid_propagate(0)
    framep4.grid_propagate(0)

    lbpnam = Label(window7,bg='white', text=("welcome to the portal, "+nam),font=("Arial Bold",13))
    lbpnam.grid(column=0, row=1)

    lbp2 = Label(window7,bg='white',text="Patients....",font=("Segoe Print",25))
    lbp2.grid(column=0, row=0)

    lbp3 = Label(window7, text="Management....",font=("Segoe Print",25 ),bg='white')
    lbp3.grid(column=2, row=0)

    lbp4 = Label(framep1, text="Appointments",font=("Arial Bold",15),bg='white')
    lbp4.grid(column=0, row=0)

    lbp5 = Label(framep2, text="Accounts",font=("Arial Bold",15),bg='white')
    lbp5.grid(column=0, row=0)

    lbp6 = Label(framep3, text="Prescriptions",font=("Arial Bold",15),bg='white')
    lbp6.grid(column=0, row=0)

    lbp7 = Label(framep4, text="Doctors",font=("Arial Bold",15),bg='white')
    lbp7.grid(column=0, row=0)

# Accounts Frame

    framep_acc41=LabelFrame(framep2,width=250,height=50)
    framep_acc41.grid(column=2,row=4)
    framep_acc41.grid_propagate(0)
    
    scrollp_acc=Scrollbar(framep_acc41,orient=VERTICAL)
    listbp_acc=Listbox(framep_acc41,height=5,width=40,font=my_font,yscrollcommand=scrollp_acc.set)

    scrollp_acc.config(command=listbp_acc.yview)
    scrollp_acc.pack(side=RIGHT,fill=Y)

    listbp_acc.pack()
    gap="|"
    le=["PC_ID","NAME","DUE","PAID"]

    listbp_acc.insert(END,f"{le[0]:>5}{gap}{le[1]:>12}{gap}{le[2]:>8}{gap}{le[3]:>8}")
    listbp_acc.insert(END,'------------------------------------------------')

    if searchLink(nam):
        for i in searchLink(nam):
            l=search02(i)
            listbp_acc.insert(END,l)
    else:
        l=search02(nam)
        listbp_acc.insert(END,l)
 

    def LINK(nam):
        linkL(nam)
       
    bp2_acc = Button(framep2, text="Link acc",width=15,command=lambda: LINK(nam))
    bp2_acc.grid(column=2,row=6,pady=10)

    
# Doctors Frame

    lbpa4 = Label(framep4, text="name search",bg='white')
    lbpa4.grid(column=0, row=2)

    txta4 = Entry(framep4, width=30)
    txta4.grid(column=2, row=2,pady=10)

    lbf4 = Label(framep4, text="search results:-", font=("Arial Bold", 10),bg='white')
    lbf4.grid(column=0, row=4)

    framep41=LabelFrame(framep4,width=250,height=50)
    framep41.grid(column=2,row=4)
    framep41.grid_propagate(0)
    
    scrollp=Scrollbar(framep41,orient=VERTICAL)
    listbp=Listbox(framep41,height=5,width=40,font=my_font,yscrollcommand=scrollp.set)

    scrollp.config(command=listbp.yview)
    scrollp.pack(side=RIGHT,fill=Y)

    listbp.pack()
    gap="|"
    le=["Dc_Id","Name","Department"]

    listbp.insert(END,f"{le[0]:>5}{gap}{le[1]:>15}{gap}{le[2]:>15}")
    listbp.insert(END,'------------------------------------------------')

    def searchpat2():
        nonlocal listbp
        if txta4.get()!="":
            l=searche4(txta4.get())
            listbp.insert(END,l)
       
    bp2 = Button(framep4, text="Search",width=15,command=searchpat2)
    bp2.grid(column=2,row=6,pady=10)

# Appointments Frame

    txtp13 = Entry(framep1, width=30)
    txtp13.grid(column=1, row=4,pady=10)
    
    lbxp10 = Label(framep1, text="patient id",bg='white')
    lbxp10.grid(column=0, row=4)


    framep11=LabelFrame(framep1,width=250,height=50)
    framep11.grid(column=0,row=6,columnspan=3)
    framep11.grid_propagate(0)

    scrollp01=Scrollbar(framep11,orient=VERTICAL)
    listbp01=Listbox(framep11,height=5,width=55,font=my_font,yscrollcommand=scrollp01.set)
    scrollp01.config(command=listbp01.yview)
    scrollp01.pack(side=RIGHT,fill=Y)
    listbp01.pack()
    gap=" | "
    lo=["Name","Doctor","Date","Time"]
    listbp01.insert(END,f"{lo[0]:>10}{gap}{lo[1]:>10}{gap}{lo[2]:>10}{gap}{lo[3]:>13}")
    listbp01.insert(END,'----------------------------------------------------------')
    
    def choosep01():
        l=searcha(txtp13.get())
        listbp01.insert(END,l)
    def clearap01():
        listbp01.delete(2,END)
        

    bp11 = Button(framep1, text="search",command=choosep01,width=10)
    bp11.grid(column=1,row=8,pady=20)

    #Prescripts

    labell=Label(framep3,text="Choose prescripts",font=("Arial Bold",10),bg='white')
    labell.grid(column=0,row=1)

    txtpr13 = Entry(framep3, width=30)
    txtpr13.grid(column=2, row=2,pady=5)
    txtpr14 = Entry(framep3, width=30)
    txtpr14.grid(column=2, row=3,pady=5)

    labell2=Label(framep3,text="Date:-",font=("Arial Bold",10),bg='white')
    labell2.grid(column=0,row=2)
    labell1=Label(framep3,text="Doctor:-",font=("Arial Bold",10),bg='white')
    labell1.grid(column=0,row=3)
    def prescript():
        prescrip_open_pat(txtpr14.get(),ID,txtpr13.get())

    bpr11 = Button(framep3, text="Search",command=prescript)
    bpr11.grid(column=2,row=8,pady=10)

    window7.config(bg='white')
    window7.geometry('1000x600')
    window7.mainloop()

def doctor(nam,ID):
    windowd=Toplevel()
    windowd.title("Doctors")
     
    imagec4=ImageTk.PhotoImage(Image.open('docc.png'))
    lbld5=Canvas(windowd,width=1350,height=800,bg="springgreen1")
    lbld5.grid_propagate(0)
    
    lbld5.create_image(0, 0 ,anchor=NW,image=imagec4)
    lbld5.grid(column=0,row=0)

    lbld=Label(lbld5,text="",font=("Segoe Print",20),bg="springgreen1",fg="white")
    lbld.grid(column=10,row=0,columnspan=4,pady=20)

    framed1=LabelFrame(lbld5,width=500,height=150)
    framed1.grid(column=4,row=1,padx=10,columnspan=2,pady=10)
    framed1.grid_propagate(0)

    framed2=LabelFrame(lbld5,width=500,height=305)
    framed2.grid(column=4,row=2,padx=10,columnspan=2,pady=10)
    framed2.grid_propagate(0)

    lbld1=Label(framed1,text="PRESCRIPTION WRITER",font=("Arial Bold",10))
    lbld1.grid(column=3,row=1,columnspan=2)

    lblc1=Label(framed1,text="ACCOUNT NO.    ",font=("Arial Bold",10))
    lblc1.grid(column=2,row=2,padx=10)

    lblc01=Label(framed1,text="Date(open)    ",font=("Arial Bold",10))
    lblc01.grid(column=2,row=3,padx=10)
    
    lblc5=Label(framed2,text="CHANGE TIME AVAIL",font=("Arial Bold",10))
    lblc5.grid(column=4,row=3,columnspan=3)
    
    lblc2=Label(framed2,text="LEAVE TIME:-      ",font=("Arial Bold",10))
    lblc2.grid(column=3,row=4)
    
    lblc3=Label(framed2,text="ARRIVE TIME:-     ",font=("Arial Bold",10))
    lblc3.grid(column=3,row=5)

    lblc6=Label(framed2,text="DATE:-     ",font=("Arial Bold",10))
    lblc6.grid(column=3,row=6)
    
    lblc4=Label(lbld5,text="THANK YOU",font=("Arial Bold",15))
    lblc4.grid(column=4,row=12)

    txtd1 = Entry(framed1, width=40)
    txtd1.grid(column=3, row=2,pady=10,columnspan=2)

    txtd01 = Entry(framed1, width=40)
    txtd01.grid(column=3, row=3,pady=10,columnspan=2)
    
    txtd2 = Entry(framed2, width=30)
    txtd2.grid(column=4, row=4,pady=10,columnspan=3)
    
    txtd3 = Entry(framed2, width=30)
    txtd3.grid(column=4, row=5,pady=10,columnspan=3)

    txtd4 = Entry(framed2, width=30)
    txtd4.grid(column=4, row=6,pady=10,columnspan=3)

    
    my_font=TkFont.Font(lbld5,family="Monaco",size=10)

    framed=LabelFrame(lbld5,width=600,height=720)
    framed.grid(column=0,row=1,rowspan=20,columnspan=2,padx=10)
    framed.grid_propagate(0)

    scrolld=Scrollbar(framed,orient=VERTICAL)
    listbd=Listbox(framed,height=32,width=80,font=my_font,yscrollcommand=scrolld.set)

    scrolld.config(command=listbd.yview)
    scrolld.pack(side=RIGHT,fill=Y)
    listbd.insert(END,"---------------------------------TODAY'S APPOINTMENTS--------------------------------")
    listbd.pack()


    def presc_win(x,y):
        prescripwr(y,x)
        
    def appoint_disp(k):
        n=searchappointments(ID)
        for i in n:
            listbd.insert(END,i)
            
    def appoint_change(k,l,n):
        write_dcc(k,l,n)

    def presc_op(ID,nam):
        prescripop(nam,ID,txtd01.get())

    bpc1 = Button(framed1, text="Create Prescript",command=lambda: presc_win(txtd1.get(),nam),width=15)
    bpc1.grid(column=3,row=4,pady=10)
    
    bpc4 = Button(framed1, text="Open Prescript",command=lambda: presc_op(txtd1.get(),nam),width=15)
    bpc4.grid(column=4,row=4,pady=10)

    bpc2 = Button(lbld5, text="Appointments",command=lambda: appoint_disp(ID),width=15)
    bpc2.grid(column=1,row=22,pady=10,columnspan=1)

    bpc3 = Button(framed2, text="CHANGE",command=lambda: appoint_change(ID,txtd3.get()+" - "+txtd2.get(),txtd4.get()),width=15)
    bpc3.grid(column=4,row=7,pady=10,columnspan=3)
        

    
    windowd.geometry("1350x750")
    windowd.mainloop()
    
def cashier():
    windowc=Toplevel()
    windowc.title("Cashier")

    imagec4=ImageTk.PhotoImage(Image.open('cashie.png'))
    lblc5=Canvas(windowc,width=920,height=600,bg="violetred1")
    
    lblc5.create_image(0, 0 ,anchor=NW,image=imagec4)
    lblc5.grid(column=0,row=0)
    

    lblc=Label(lblc5,font=("Segoe Print",20),bg="orange",fg="white")
    lblc.grid(column=10,row=0,columnspan=6,pady=20)

    framec=LabelFrame(lblc5,width=600,height=720)
    framec.grid(column=0,row=2,rowspan=20,padx=10)
    framec.grid_propagate(0)

    lblc1=Label(lblc5,text="ACCOUNT No.",font=("Arial Bold",10))
    lblc1.grid(column=3,row=2,pady=20)
    
    lblc2=Label(lblc5,text="PAYMENT Method",font=("Arial Bold",10))
    lblc2.grid(column=3,row=4)
    
    lblc3=Label(lblc5,text="AMOUNT RECIEVED",font=("Arial Bold",10))
    lblc3.grid(column=3,row=5)
    
    lblc4=Label(lblc5,text="THANK YOU",font=("Arial Bold",15))
    lblc4.grid(column=4,row=12)

    txtc1 = Entry(lblc5, width=30)
    txtc1.grid(column=4, row=2,pady=10)
    
    txtc2 = Entry(lblc5, width=30)
    txtc2.grid(column=4, row=4,pady=10)
    
    txtc3 = Entry(lblc5, width=30)
    txtc3.grid(column=4, row=5,pady=10)

    framec1=LabelFrame(lblc5,width=600,height=720)
    framec1.grid(column=3,row=7,rowspan=5,columnspan=3)
    framec1.grid_propagate(0)

    def displayc():
        l=searchTR02(txtc1.get())
        listbc.delete(2,END)
        listbc1.delete(2,END)
        
        for i in l[0]:
            listbc.insert(END,i)
        for i in l[1]:
            listbc1.insert(END,i)
            
    def payc():
        nonlocal txtc3
        if int(txtc3.get())>=int(listbc.get(ANCHOR)[31:].lstrip()):
            l=int(txtc3.get())-int(listbc.get(ANCHOR)[31:].lstrip())
            
            txtc3.delete(first=0,last=20)
            txtc3.insert(0,str(l))
            
            up_paidIn(int(listbc.get(ANCHOR)[31:].lstrip()),txtc1.get())
            up_paidTR(listbc.get(ANCHOR)[1:5])
            listbc.delete(ANCHOR)
            displayc()

    bpc1 = Button(lblc5, text="Search",command=displayc,width=10)
    bpc1.grid(column=4,row=3,pady=10)
    
    bpc2 = Button(lblc5, text="PAY",command=payc,width=10)
    bpc2.grid(column=4,row=6,pady=10)
    
    my_font=TkFont.Font(lblc5,family="Monaco",size=10)
    
    scrollc=Scrollbar(framec,orient=VERTICAL)
    listbc=Listbox(framec,height=40,width=80,font=my_font,yscrollcommand=scrollc.set)

    scrollc.config(command=listbc.yview)
    scrollc.pack(side=RIGHT,fill=Y)
    
    listbc.insert(END,"------------------------------------INVOICE------------------------------------")
    listbc.pack()
    gap="|"
    i=("T_ID","ACCOUNT","DETAILS","PRICE")
    listbc.insert(END,f"{i[0]:5}{gap}{i[1]:>18}{gap}{i[2]:>30}{gap}{i[3]:>17}")
    
    scrollc1=Scrollbar(framec1,orient=VERTICAL)
    listbc1=Listbox(framec1,height=20,width=80,font=my_font,yscrollcommand=scrollc1.set)

    scrollc1.config(command=listbc1.yview)
    scrollc1.pack(side=RIGHT,fill=Y)

    listbc1.insert(END,"------------------------------PAYMENT HISTORY-----------------------------")
    listbc1.pack()
    listbc1.insert(END,f"{i[0]:5}{gap}{i[1]:>18}{gap}{i[2]:>30}{gap}{i[3]:>17}")

    windowc.geometry('1350x750')
    windowc.mainloop()
    
