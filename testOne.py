import quandl
import pandas as pd 
import csv
import sys

names = pd.read_csv("BSE_metadata.csv") 
# print(names.head())

stox = ''
name = input('Enter stock to find\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('BSE_metadata.csv', "r"), delimiter=",")

#loop through the csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if name.lower() in row[1].lower():
        stox = row[0]
        break

# print(stox)

query = "BSE/" + stox
quandl.ApiConfig.api_key = 'QbEcRXcx-ezgQ6qvye4h'

data = quandl.get(query)
print(data.tail())

# turnover value
from datetime import date, datetime
todays_date = date.today()
print("Current date: ", todays_date)
print("Current year:", todays_date.year)
print("Current month:", todays_date.month)
print("Current day:", todays_date.day)

da = str(int(todays_date.year)-1) + "-" + str(todays_date.month) + "-" + str(todays_date.day)
print(da)
print(data.loc[da])
# # # filter rows on the basis of date
# newdf = (data['Date'] > da) & (data['date_added'] <= todays_date)
# newdf = data.loc[newdf]
# print(newdf)