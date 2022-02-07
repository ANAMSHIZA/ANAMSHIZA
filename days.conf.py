import datetime
from datetime import time
from datetime import date
from apscheduler.scheduler import Scheduler

jour_ouvrables=[] 
jour_semi_ouvrables=[]   

def daysGenerator_ouvrables():
    openDays=[0,1,2,4]
    return(openDays)

def daysGenerator_semi_ouvrables():
    semi_openDays=[2,5]
    return(semi_openDays)

jour_ouvrables=daysGenerator_ouvrables()
jour_semi_ouvrables=daysGenerator_semi_ouvrables()
#print(jour_ouvrables)
#print(jour_semi_ouvrables)

time=datetime.datetime.now()
wd=time.weekday()
#print(wd)

if wd==jour_ouvrables[0] or wd==jour_ouvrables[1] or wd==jour_ouvrables[2] or wd==jour_ouvrables[3]:
    print("jour ouvrable")
else:
    print("jour semi_ouvré")
    
#jour_ouvrables[0]="lundi"
#jour_ouvrables[1]="mardi"
#jour_ouvrables[2]="jeudi"
#jour_ouvrables[3]="vendredi"
#jour_semi_ouvrables[0]="mercredi"
#jour_semi_ouvrables[1]="samedi"
#print(jour_ouvrables[2])

h=time.hour
m=time.minute

#sonnerie jours ouvrables
if wd==0 or wd==1 or wd==3 or wd==4 :
    if h==8 and m==20 or h==8 and m==25 :
        print("sonnerie")
    elif h==9 and m==20 or h==9 and m==25 :
        print("sonnerie")
    elif h==10 and m==25 or h==10 and m==35 :
        print("sonnerie")
    elif h==11 and m==30 or h==11 and m==35 :
        print("sonnerie")
    elif h==12 and m==30 or h==12 and m==50 or h==12 and m==55 :
        print("sonnerie")
    elif h==13 and m==45 or h==13 and m==50 :
        print("sonnerie")
    elif h==14 and m==45 or h==14 and m==50 :
        print("sonnerie")
    elif h==15 and m==45 or h==15 and m==55 :
        print("sonnerie")
    elif h==16 and m==0 or h==16 and m==55 :
        print("sonnerie")
    elif h==17 and m==0 or h==17 and m==55 :
        print("sonnerie")
    elif h==18 and m==0 :
        print("sonnerie")
    else:
        print("pas de sonnerie")
        
#sonnerie jours semi-ouvrés
if wd==2 or wd==5 :
    if h==8 and m==20 or h==8 and m==25 :
        print("sonnerie")
    elif h==9 and m==20 or h==9 and m==25 :
        print("sonnerie")
    elif h==10 and m==25 or h==10 and m==35 :
        print("sonnerie")
    elif h==11 and m==30 or h==11 and m==35 :
        print("sonnerie")
    elif h==12 and m==30
        print("sonnerie")
    else:
        print("pas de sonnerie")
