import datetime
from datetime import time

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
    
jour_ouvrables[0]="lundi"
jour_ouvrables[1]="mardi"
jour_ouvrables[2]="jeudi"
jour_ouvrables[3]="vendredi"
jour_semi_ouvrables[0]="mercredi"
jour_semi_ouvrables[1]="jeudi"
#print(jour_ouvrables[2])
