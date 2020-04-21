from sys import argv
import pandas as pd 
import datetime
import collections

desiredMonth = argv[1]
desiredWeek = argv[2]
  
megasenaResults = pd.read_csv("my_csv.csv") 

monthResults = megasenaResults[megasenaResults['month'] == int(desiredMonth)]
linesByMonthAndWeek = monthResults[monthResults['weekMonth'] == int(desiredWeek)]

monthNumbers = []

for index, row in linesByMonthAndWeek.iterrows():

    monthNumbers.append(row['bola 1'])
    monthNumbers.append(row['bola 2'])
    monthNumbers.append(row['bola 3'])
    monthNumbers.append(row['bola 4'])
    monthNumbers.append(row['bola 5'])
    monthNumbers.append(row['bola 6'])


repeatedNumbers = collections.Counter(monthNumbers).most_common(6)
listOfNumbers = []

for number in repeatedNumbers:
    listOfNumbers.append(number[0])

print(listOfNumbers)