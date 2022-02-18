import datetime
from datetime import date, datetime
import time
from time import sleep
import os
import pandas
#fichier csv des heures de sonnerie
heures_j_ouvrables=pandas.read_csv("heures_jours_ouvres.csv")
heures_j_semi_ouvrables=pandas.read_csv("heures_semi_ouvres.csv")

#jours ouvrables/semi-ouvrables
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

time=datetime.now()
wd=time.weekday()
#print(wd)

#if wd==jour_ouvrables[0] or wd==jour_ouvrables[1] or wd==jour_ouvrables[2] or wd==jour_ouvrables[3]:
    #print("jour ouvrable")
#else:
    #print("jour semi_ouvré")

h=time.hour
m=time.minute
dt= datetime.today()
seconds= dt.timestamp()

print("h=",h,"wd=",wd,"m=",m)
#sonnerie jours ouvrables
if wd==0 or wd==1 or wd==3 or wd==4:
    if h==8 and m==20 or h==8 and m==25 :
        #os.system("Sonnerie.mp3")
        sleep(5.00)
        print("dring")
        #os.system("taskkill/IM<Groove Musique>")
        
    elif h==9 and m==20 or h==9 and m==25 :
        os.system("Sonnerie.mp3")
    elif h==10 and m==25 or h==10 and m==35 :
        os.system("Sonnerie.mp3")
    elif h==11 and m==30 or h==11 and m==39 :
        os.system("Sonnerie.mp3")
    elif h==12 and m==30 or h==12 and m==50 or h==12 and m==55 :
        os.system("Sonnerie.mp3")
    elif h==13 and m==45 or h==13 and m==50 :
        os.system("Sonnerie.mp3")
    elif h==14 and m==45 or h==14 and m==50 :
        os.system("Sonnerie.mp3")
    elif h==15 and m==45 or h==15 and m==55 :
        os.system("Sonnerie.mp3")
    elif h==16 and m==0 or h==16 and m==55 :
        os.system("Sonnerie.mp3")
    elif h==17 and m==0 or h==17 and m==55 :
        os.system("Sonnerie.mp3")
    elif h==18 and m==0 :
        os.system("Sonnerie.mp3")
    else:
        print("pas de sonnerie")
        
#sonnerie jours semi-ouvrés
if wd==2 or wd==5:
    if h==8 and m==20 or h==8 and m==25 :
        os.system("Sonnerie.mp3")
    elif h==9 and m==20 or h==9 and m==25 :
        os.system("Sonnerie.mp3")
    elif h==10 and m==25 or h==10 and m==35 :
        os.system("Sonnerie.mp3")
    elif h==11 and m==30 or h==11 and m==35 :
        os.system("Sonnerie.mp3")
    elif h==12 and m==30 :
        os.system("Sonnerie.mp3")
    else:
        print("pas de sonnerie")
