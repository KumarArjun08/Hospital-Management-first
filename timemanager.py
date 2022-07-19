from appointmanager1 import *
from appointmanager2 import *

def appoint_time(date,k,a,b):
    h1=int(a.split(":")[0])
    h2=int(b.split(":")[0])
    m1=int(a.split(":")[1])
    m2=int(b.split(":")[1])

    l=[]
    for i in range(h2-h1+1):
      if i+h1<h2:
          while m1<60:
              if m1!=45 and m1!=0:
                  l.append(str(h1+i)+":"+str(m1)+" - "+str(h1+i)+":"+str(m1+15))
                  m1+=15
              elif m1==0:
                  l.append(str(h1+i)+":"+"00"+" - "+str(h1+i)+":"+str(m1+15))
                  m1+=15
              else:
                  l.append(str(h1+i)+":"+str(m1)+" - "+str(h1+i+1)+":"+"00")
                  m1+=15
          m1=0
      elif i+h1==h2:
          while m1<m2:
              if m1!=45 and m1!=0:
                  l.append(str(h1+i)+":"+str(m1)+" - "+str(h1+i)+":"+str(m1+15))
                  m1+=15
              elif m1==0:
                  l.append(str(h1+i)+":"+"00"+" - "+str(h1+i)+":"+str(m1+15))
                  m1+=15
              else:
                  l.append(str(h1+i)+":"+str(m1)+" - "+str(h1+i+1)+":"+"00")
                  m1+=15
          m1=0
    poptime=searchtime(k)
    for i in poptime:
        for j in l:
            if j==str(i[0]) and str(i[1])==str(date) and i[2]=="Active":
                l.remove(j)
    return l



