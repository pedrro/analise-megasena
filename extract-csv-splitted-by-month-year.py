import pandas as pd 
import datetime
  
megasenaResults = pd.read_csv("megasena.csv") 

monthValues = []
yearValues = []
weekMonth = []

for index, row in megasenaResults.iterrows():
    datee = datetime.datetime.strptime(row["Data"], "%d/%m/%Y")
    monthValues.append(datee.month)
    yearValues.append(datee.year)
    num = (datee.day-1)//7+1
    weekMonth.append(num)

megasenaResults["month"] = monthValues
megasenaResults["year"] = yearValues   
megasenaResults["weekMonth"] = weekMonth

megasenaResults.to_csv('my_csv.csv', mode='a', header=True)
