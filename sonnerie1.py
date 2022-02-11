import datetime
from datetime import date, datetime
import time
from time import sleep
import os

print(date.today())

os.system("Sonnerie.mp3")

dt= datetime.today()
seconds= dt.timestamp()
print(seconds)
for i in range(10):
          dt= datetime.today()
          seconds= dt.timestamp()
          print(seconds)
          sleep(1.00)
