import datetime 
from datetime import date
import os
import pandas 

jour_j_non_ouvrables=pandas.read_csv("lesvacances.csv")
print(jour_j_non_ouvrables["month"][0])
print("informations lues :")
for s in jour_j_non_ouvrables:
  print(s)
  print(jour_j_non_ouvrables[s])
  
jour_j_non_ouvrables2=pandas.read_csv("lesjoursfériés.csv")
print(jour_j_non_ouvrables2["month"][0])
print("informations lues :")
for s in jour_j_non_ouvrables2:
    print(s)
    print(jour_j_non_ouvrables2[s])
      
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
if wd==0 or wd==1 or wd==2 or wd==3 or wd==4 or wd==5 :
    day= time.day
    month=time.month
    #on parcourt le fichier CSV et on teste le jour où c'est les vacances
    for i in range(len(jour_j_non_ouvrables["wd"])):
        print("month=%d day=%d son=%s"%(jour_j_non_ouvrables["month"][i],jour_j_non_ouvrables["day"][i],jour_j_non_ouvrables["sonnerie.py"][i] ))
        if(month==jour_j_non_ouvrables["month"][i] and day==jour_j_non_ouvrables["day"][i]):
            print("C'est les vacances :",jour_j_non_ouvrables["sonnerie.py"][i])
    
#les jours fériés 
if wd==0 or wd==1 or wd==2 or wd==3 or wd==4 or wd==5 :
    day= time.day
    month=time.month
    #on parcourt le fichier CSV et on teste le jour où c'est fériés
    for i in range(len(jour_j_non_ouvrables2["wd"])):
        print("month=%d day=%d son=%s"%(jour_j_non_ouvrables2["month"][i],jour_j_non_ouvrables2["day"][i],jour_j_non_ouvrables2["sonnerie.py"][i] ))
        if(month==jour_j_non_ouvrables2["month"][i] and day==jour_j_non_ouvrables2["day"][i]):
            print("C'est un jour férié :",jour_j_non_ouvrables2["sonnerie.py"][i])
