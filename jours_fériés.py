import datetime 
from datetime import date
import os

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

#les vacances
if wd==0 or wd==1 or wd==2 or wd==3 or wd==4 or wd==5: 
    day = time.day
    month = time.month
    print("month=",month,"day=",day)
    if month==2 and day==21 or month==2 and day==22 or month==2 and day==23 or month==2 and day==24 or month==2 and day==25 or month==2 and day==26:
        print ("Vacances donc pas de sonnerie")
    elif month==2 and day==28 or month==3 and day==1 or month==3 and day==2 or month==3 and day==3 or month==3 and day==4 or month==3 and day==5:
        print ("Vacances donc pas de sonnerie")
    elif month==4 and day==25 or month==4 and day==26 or month==4 and day==27 or month==4 and day==28 or month==4 and day==29 or month==4 and day==30:
        print ("Vacances donc pas de sonnerie")
    elif month==5 and day==2 or month==5 and day==3 or month==5 and day==4 or month==5 and day==5 or month==5 and day==6 or month==5 and day==6:
        print ("Vacances donc pas de sonnerie")
    elif month==7:
        print ("Vacances donc pas de sonnerie")
    elif month==8: 
        print ("Vacances donc pas de sonnerie")
    elif month==10 and day==24 or month==10 and day==25 or month==10 and day==26 or month==10 and day==27 or month==10 and day==28 or month==10 and day==29:
        print ("Vacances donc pas de sonnerie")
    elif month==10 and day==31 or month==11 and day==1 or month==11 and day==2 or month==11 and day==3 or month==11 and day==4 or month==11 and day==5:
        print ("Vacances donc pas de sonnerie")
    elif month==12 and day==19 or month==12 and day==20 or month==12 and day==21 or month==12 and day==22 or month==12 and day==23 or month==12 and day==24:
         print ("Vacances donc pas de sonnerie")
    elif month==12 and day==26 or month==12 and day==27 or month==12 and day==28 or month==12 and day==29 or month==12 and day==30 or month==12 and day==31:
         print ("Vacances donc pas de sonnerie")

#les jours fériés
    if month==4 and day==18:
        print ("Fériés donc pas de sonnerie")
    elif month==5 and day==26:
        print ("Fériés donc pas de sonnerie")
    elif month==6 and day==6:
        print ("Fériés donc pas de sonnerie")
    elif month==11 and day==11:
        print ("Fériés donc pas de sonnerie")
