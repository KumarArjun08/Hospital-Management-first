import csv
import datetime
import tkinter as tk
#importing the required modules
#Aliases for all the storage files
fn = 'appoint.csv'
dn = 'doctor.csv'
pn = 'patient.csv'

#Appointment Record Creator
def writea(b,c,d,e,g):
    l = []
    global fn
    with open(fn, 'a+') as f:
        
        csw = csv.writer(f, lineterminator='\n')
        f.seek(0)
        l = list(csv.reader(f))
        if len(l) == 0:
            a = 101
        else:
            a = int(l[-1][0]) + 1
        rec = [a,b,c,d,e,g]
        csw.writerow(rec)
        print("Appointment created sucessfully")

#Searching the Files
def reada():
    global fn
    global dn
    global pn
    rec = []
    hdr = 'AppId\tPatientId\tPatient Name\tDoctor Id\tDoctor Name\tAppointDate\tAppointTime\tStatus'
    with open(fn, 'r') as f, open(dn, 'r') as d, open(pn, 'r') as p:
        csr = csv.reader(f)
        csrd = list(csv.reader(d))
        csrp = list(csv.reader(p))
        print(hdr)
        for i in csr:
            drnm = ''
            pnm = ''
            for j in csrp:
                if j[0] == i[1]:
                    pnm = j[1]
                    break
            for j in csrd:
                if j[0] == i[2]:
                    drnm = j[1]
                    break

            res=(i[0], '\t', i[1], '\t', pnm, '\t', i[2], '\t', drnm, '\t', i[3], '\t', i[4], '\t', i[5])
            print(res)
            return res

#Basiclly a single Search
def searcha(pid):
    global fn
    global dn
    global pn
    with open(fn, 'r') as f, open(dn, 'r') as d, open(pn, 'r') as p:
        csr = csv.reader(f)
        csrd = list(csv.reader(d))
        csrp = list(csv.reader(p))
        l=[]
        flag = False
        for i in csr:
         if i[1] == pid:
           flag = True
           l=i
           drnm = ''
           pnm = ''
           for j in csrp:
              if j[0] == i[1]:
                 pnm = j[1]
                 pnm0=pnm.split()
                 break
           for j in csrd:
              if j[0] == i[2]:
                 drnm = j[1]
                 drnm0=drnm.split()
                 break
       
        
        if flag == False:
            res=('No Record')
            print (res)
            return res
        else:
            gap=" | "
            t="Dr. "
            drnm0[1]=t+drnm0[1]
            res=(f"{pnm0[0]:>10}{gap}{drnm0[1]:>10}{gap}{l[4]:>10}{gap}{l[3]:>13}")
            print(res)
            return res

         
#Updating Values
def updatea(ID,s,val):
    global fn
    with open(fn, 'r') as f:
        flag = False
        csr = csv.reader(f)
        reclst = list(csr)
        for i in range(len(reclst)):
            if int(reclst[i][0]) == ID:
                print(reclst[i])
                flag = True
                if s == 'time':
                    reclst[i][3] = val
                elif s == 'date':
                    reclst[i][4] = val
                elif s == 'status':
                    reclst[i][5] = val

    with open(fn, 'w') as f:
        csw = csv.writer(f, lineterminator='\n')
        csw.writerows(reclst)

    if flag:
        print('Record updated')
    else:
        print('Record not found')


def deletea(ID):
    global fn
    with open(fn, 'r') as f:
        flag = False
        csr = csv.reader(f)
        reclst = list(csr)
        for i in range(len(reclst)):
            if int(reclst[i][0]) == ID:
                flag = True
                reclst.pop(i)
                break
    with open(fn, 'w') as f:
        csw = csv.writer(f, lineterminator='\n')
        csw.writerows(reclst)

    if flag:
        print('Record deleted')
    else:
        print('Record not found')

def searchtime(did):
    global fn
    global dn
    global pn
    with open(fn, 'r') as f, open(dn, 'r') as d, open(pn, 'r') as p:
        csr = csv.reader(f)
        csrd = list(csv.reader(d))
        csrp = list(csv.reader(p))
        l=[]
        k=[]
        flag = False
        for i in csr:
         if i[2] == did:
           flag = True
           l.append([i[3],i[4],i[5]])
        
    return l

def searchappointments(did):
    global fn
    global dn
    global pn
    m=str(datetime.datetime.now())[:10].split("-")
    da=""
    da=m[2]+"/"+m[1]+"/"+m[0]
    with open(fn, 'r') as f, open(dn, 'r') as d, open(pn, 'r') as p:
        csr = csv.reader(f)
        csrd = list(csv.reader(d))
        csrp = list(csv.reader(p))
        l=[]
        k=[]
        flag = False
        for i in csr:
         if i[2] == str(did) and i[4]==da:
           flag = True
           gap="|"
           l.append(f"{i[0]:>3}{gap}{i[1]:>5}{gap}{i[2]:>5}{gap}{i[3]:>15}{gap}{i[4]:>15}{gap}{i[5]:>15}")
        
    return l






