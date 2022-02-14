import datetime
from datetime import date, datetime
import time
from time import sleep
import os

#h=time.hour()
#m=time.minute()
dt= datetime.today()
seconds= dt.timestamp()

while True:
    dt= datetime.today()
    print("dt=",dt)
    sleep(1)
