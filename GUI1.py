from tkinter import *
from GUI2 import *
from f1 import *
from PIL import ImageTk,Image

#Creating the first display screen
def lgn_disp1():
    window0=Tk()
    window0.title("XYZ HOSPITAL")
    
    image2=ImageTk.PhotoImage(Image.open('FINALLOGIN.png'))

    img_1=ImageTk.PhotoImage(Image.open('button.png'))
    
    lbc1=Canvas(window0,width=1350,height=720,bg="RoyalBlue3")
    lbc1.grid_propagate(0)
    lbc1.create_image(0,0 ,anchor=NW,image=image2)
    lbc1.grid(column=0,row=0)

      
    def clik():
        lgn_disp(window0)

    frame11=LabelFrame(lbc1,width=950,height=250)
    #frame11.grid(column=4,row=4,padx=175,columnspan=3)
    #frame11.grid_propagate(0)


    btn0 = Button(lbc1, image=img_1, command=clik,borderwidth=0)
    btn0.grid(column=5,row=10,pady=565,padx=780)

    btn01 = Button(lbc1, text="QUIT", command=window0.quit,width=30,height=2)
    #btn01.grid(column=5,row=11,pady=2)
    
    window0.geometry('1350x750')
    window0.mainloop()

#Login Screen
def lgn_disp(prev):
    window = Toplevel(prev)
    window.title("XYZ HOSPITAL")
    
    image1=ImageTk.PhotoImage(Image.open('dispp.png'))
    
    lbc=Canvas(window,width=400,height=200,bg="white")
    lbc.grid_propagate(0)
    lbc.create_image(0, 0 ,anchor=NW,image=image1)
    lbc.grid(column=0,row=0)
    
    lb1 = Label(lbc, text="enter credentials", font=("Arial Bold", 15),bg="White")
    lb1.grid(column=0, row=0)

    txt1 = Entry(lbc, width=25)
    txt1.grid(column=1, row=3,pady=2)

    txt2 = Entry(lbc, width=25)
    txt2.grid(column=1, row=5)

    txt1.insert(0, "Administrator")
    txt2.insert(0, "passwd")

    x = (txt1.get(),txt2.get())

    def check():
        try:
            int(txt2.get())
            if (int(txt2.get()),(txt1.get())) in select():
                nam=txt1.get()
                ID=int(txt2.get())
                doctor(nam,ID)
            elif (txt1.get(),txt2.get()) in search_all():
                patient(txt1.get(),txt2.get())
            else:
                txt1.insert(0, "Administrator")
                txt2.insert(0, "incorrect passwd")

        except ValueError:
            if txt1.get() == "guest":
               patient("guest")
            elif txt1.get() == "Administrator" and txt2.get() == "passwd":
               post_lg("Administrator..")
            elif (txt1.get(),txt2.get()) in search_all():
               patient(txt1.get())
            else:
               txt1.insert(0, "Administrator")
               txt2.insert(0, "incorrect passwd")
               
    btn = Button(lbc, text="submit", command=check,width=10)
    btn.grid(column=1,row=8,pady=2)
    
    window.config(bg="White")
    window.geometry('350x150')
    window.mainloop()

#Administrator Mode Options Menu
def post_lg(x):
    window1 = Toplevel()
    window1.title("depatments")

    image2=ImageTk.PhotoImage(Image.open('dispp.png'))
    
    lbc1=Canvas(window1,width=400,height=200,bg="white")
    lbc1.grid_propagate(0)
    lbc1.create_image(0, 0,anchor=NW,image=image2)
    lbc1.grid(column=0,row=0)
    

    lb3 = Label(lbc1, text="enter your requirement", font=("Arial Bold", 10),bg="white")
    lb3.grid(column=0, row=2)

    lb4 = Label(lbc1, text="welcome "+x, font=("Segoe Print", 15),bg="white")
    lb4.grid(column=0, row=0)

    click = StringVar(window1)
    click.set("accounts")

    drop = OptionMenu(lbc1,click, "accounts", "appointments", "employee data", "pharmacy","cashier")
    drop.config(width=11)
    drop.grid(column=1, row=2)

    def select():
        if click.get() == "accounts":
            acc()
        if click.get() == "appointments":
            pre_appoint()
        if click.get() == "employee data":
            empl()
        if click.get() == "pharmacy":
            pharm()
        if click.get() == "cashier":
            cashier()
            
    b1 = Button(lbc1, text="select", command=select,width=14)
    b1.grid(column=1, row=4)
    
    window1.config(bg="white")
    window1.geometry('415x150')
    window1.mainloop()
