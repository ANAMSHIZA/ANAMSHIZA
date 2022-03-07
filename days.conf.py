import datetime
from datetime import date, datetime
import time
from time import sleep
import os
import pandas

#fichiers csv des heures de sonnerie :
    #jours ouvrés :
heures_j_ouvrables=pandas.read_csv("heures_jours_ouvres.csv")
print(heures_j_ouvrables["heures"][0])
print("informations lues :")
for s in heures_j_ouvrables:
    print(s)
    print(heures_j_ouvrables[s])
    
    #jours semi_ouvrés :
heures_j_semi_ouvrables=pandas.read_csv("heures_semi_ouvres.csv")
print(heures_j_semi_ouvrables["heures"][0])
print("informations lues :")
for s in heures_j_semi_ouvrables:
    print(s)
    print(heures_j_semi_ouvrables[s])

#jours ouvrables/semi-ouvrables
def daysGenerator_ouvrables():
    openDays=[0,1,3,4]
    return(openDays)

def daysGenerator_semi_ouvrables():
    semi_openDays=[2,5]
    return(semi_openDays)

temps=datetime.now()
wd=temps.weekday()
"""
test :
print(wd)

if wd==jour_ouvrables[0] or wd==jour_ouvrables[1] or wd==jour_ouvrables[2] or wd==jour_ouvrables[3]:
    print("jour ouvrable")
else:
    print("jour semi_ouvrés")
"""
h=temps.hour
m=temps.minute
dt= datetime.today()
seconds= dt.timestamp()

while True:
    print("\nMaintenant il est : h=",h,"wd=",wd,"m=",m,"s=",seconds,"\n")
    #sonnerie jours ouvrables :
    if wd==0 or wd==1 or wd==3 or wd==4:
        #on parcourt le fichier CSV et on teste si l'heure actuelle y est présente
        for i in range(len(heures_j_ouvrables["heures"])):
            #print("h=%d m=%d s=%d son=%s"%(heures_j_ouvrables["heures"][i],heures_j_ouvrables["minutes"][i],heures_j_ouvrables["secondes"][i],heures_j_ouvrables["fichier_sonnerie"][i] ))
            if(h==heures_j_ouvrables["heures"][i] and m==heures_j_ouvrables["minutes"][i]) and seconds==heures_j_ouvrables["secondes"][i]:
                print("C'est l'heure de jouer :",heures_j_ouvrables["fichier_sonnerie"][i])
                os.system(heures_j_ouvrables["fichier_sonnerie"][i])
    wd=temps.weekday()
    h=temps.hour
    m=temps.minute
    dt= datetime.today()
    seconds= dt.timestamp()
                
    #sonnerie jours semi-ouvrés :
    if wd==2 or wd==5:
        #on parcourt le fichier CSV et on teste si l'heure actuelle y est présente
        for i in range(len(heures_j_semi_ouvrables["heures"])):
            #print("h=%d m=%d s=%d son=%s"%(heures_j_semi_ouvrables["heures"][i],heures_j_semi_ouvrables["minutes"][i],heures_j_ouvrables["secondes"][i],heures_j_semi_ouvrables["fichier_sonnerie"][i] ))
            if(h==heures_j_semi_ouvrables["heures"][i] and m==heures_j_semi_ouvrables["minutes"][i]) and seconds==heures_j_ouvrables["secondes"][i]:
                print("C'est l'heure de jouer :",heures_j_ouvrables["fichier_sonnerie"][i])
                os.system(heures_j_ouvrables["fichier_sonnerie"][i])




