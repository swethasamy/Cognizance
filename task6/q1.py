
import pandas as pd

account = pd.read_csv("onelinefile.txt",
                      delimiter = ',')
  

account.to_csv('onelinefile.csv',
               index = None)
import csv

with open('onelinefile.csv', newline='') as myFile:
    reader = csv.reader(myFile, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)