import datetime
from datetime import date, datetime
import time
from time import sleep
import os
import pandas

#Partie Cécile :
#fichiers csv des heures de sonnerie :
    #pour les jours ouvrés :
heures_j_ouvrables=pandas.read_csv("heures_jours_ouvres.csv")

    #pour les jours semi_ouvrés :
heures_j_semi_ouvrables=pandas.read_csv("heures_semi_ouvres.csv")

temps=datetime.now() #on récupère l'heure et le jour actuels dans une variable temps
wd=temps.weekday() #''le jour (0=lundi,1,2,4,5,6 ou 7=dimanche) dans wd

"""
test :
print(wd)

if wd==jour_ouvrables[0] or wd==jour_ouvrables[1] or wd==jour_ouvrables[2] or wd==jour_ouvrables[3]:
    print("jour ouvrable")
else:
    print("jour semi_ouvrés")
"""

#boucle pour jouer la sonnerie pendant jours ouvrés
while (True): #boucle TANT QUE infinie
    x=datetime.now()
    h=x.hour #on récupère l'heure actuelle dans h (mise à jour à chaque itération)
    m=x.minute #on récupère les minutes dans m
    wd=temps.weekday()
    dt= datetime.today()
    print("\nMaintenant il est : h=",h,"wd=",wd,"m=",m,"dt=",dt,"\n")

    #sonnerie jours ouvrables :
    if wd==0 or wd==1 or wd==3 or wd==4:
        #on parcourt le fichier CSV et on teste si l'heure actuelle y est présente
        for i in range(len(heures_j_ouvrables["heures"])):
            #print("h=%d m=%d son=%s"%(heures_j_ouvrables["heures"][i],heures_j_ouvrables["minutes"][i],heures_j_ouvrables["fichier_sonnerie"][i] ))
            if(h==heures_j_ouvrables["heures"][i] and m==heures_j_ouvrables["minutes"][i]):
                print("C'est l'heure de jouer :",heures_j_ouvrables["fichier_sonnerie"][i])
                temps_debut=datetime.now()
                print("debut du programme, seconde=",temps_debut.second)
                #on joue la sonnerie
                os.system(heures_j_ouvrables["fichier_sonnerie"][i])
                
                #seconde boucle pour arrêter la sonnerie au bout d'un temps défini
                while(True):
                    x=datetime.now()
                    duree=x-temps_debut #on calcule le temps d'exécution
                    print("temps ecoulé : ", duree.total_seconds()," s")
                    secondes=duree.total_seconds() #on stocke ce temps dans secondes
                    minute= (secondes//60)%60

                    if(secondes >=5) : #arrêt au bout de 5s
                        print("Temps de 5s dépassé, on quitte")
                        break #on casse la boucle
    
    sleep(1.00) #on attend 1s et on recommence à partir de la 1ère boucle while
      
#pour jouer la sonnerie pendant jours semi-ouvrés (même principe) :
    if wd==2 or wd==5:
        #on parcourt le fichier CSV et on teste si l'heure actuelle y est présente
        for i in range(len(heures_j_semi_ouvrables["heures"])):
            #print("h=%d m=%d son=%s"%(heures_j_semi_ouvrables["heures"][i],heures_j_semi_ouvrables["minutes"][i],heures_j_semi_ouvrables["fichier_sonnerie"][i] ))
            if(h==heures_j_semi_ouvrables["heures"][i] and m==heures_j_semi_ouvrables["minutes"][i]):
                print("C'est l'heure de jouer :",heures_j_semi_ouvrables["fichier_sonnerie"][i])
                
                temps_debut=datetime.now()
                print("debut du programme, seconde=",temps_debut.second)
                os.system(heures_j_semi_ouvrables["fichier_sonnerie"][i])
                
                while(True):
                    x=datetime.now()
                    
                    duree=x-temps_debut
                    print("temps ecoulé : ", duree.total_seconds()," s")
                    secondes=duree.total_seconds()
                    minute= (secondes//60)%60

                    if(secondes >=5) : #arrêt au bout de 5s
                        print("Temps de 5s dépassé, on quitte")
                        break

    sleep(1.00)

#Partie Anam :
jour_j_non_ouvrables=pandas.read_csv("lesvacances.csv")
print(jour_j_non_ouvrables["month"][0])
print("informations lues :")
for d in jour_j_non_ouvrables:
  print(d)
  print(jour_j_non_ouvrables[d])
  
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
            wd=time.weekday()

#les jours fériés 
if wd==0 or wd==1 or wd==2 or wd==3 or wd==4 or wd==5 :
    day= time.day
    month=time.month
    #on parcourt le fichier CSV et on teste le jour où c'est fériés
    for i in range(len(jour_j_non_ouvrables2["wd"])):
        print("month=%d day=%d son=%s"%(jour_j_non_ouvrables2["month"][i],jour_j_non_ouvrables2["day"][i],jour_j_non_ouvrables2["sonnerie.py"][i] ))
        if(month==jour_j_non_ouvrables2["month"][i] and day==jour_j_non_ouvrables2["day"][i]):
            print("C'est un jour férié :",jour_j_non_ouvrables2["sonnerie.py"][i])
            wd=time.weekday()
