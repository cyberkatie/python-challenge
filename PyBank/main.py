#imports dependencies
import os
import csv
import pandas as pd
import shutil

#create empty lists
profits_losses = []
dates = []

#open csv files
with open('Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)

    #appends values into the lists
    for line in csvreader:
        profits_losses.append(line[1])
        dates.append(line[0])

#sets profits/losses to int data type
for i in range(len(profits_losses)):
    profits_losses[i] = int(profits_losses[i])

#import csv as a dataframe
df = pd.read_csv('Resources/budget_data.csv')

temp = []
for index, i in enumerate(df['Profit/Losses'][1:]):
    temp.append(i - df['Profit/Losses'][index])

avg_change = (sum(temp)/len(temp))

#calculate the total profits
total = 0
for i in range(len(profits_losses)):
    total += profits_losses[i]

#calculate the average change
change = []
for i in range(len(profits_losses)):
    changes = profits_losses[i] - profits_losses[i-1]
    change.append(changes)

#find the values of the max profit increase and decrease
max_val = max(change)
min_val = min(change)

#find the index of the values
max_ind = change.index(max_val)
min_ind = change.index(min_val)

#print report

print("financial analysis")
print(f"total months: {len(dates)}")
print(f"total: ${total}")
print(f"average change: ${avg_change}")
print(f"Greatest increase in profits: ${max_val} on {dates[max_ind]}")
print(f"Greatest decrease in profits: ${min_val} on {dates[min_ind]}")
#export to a .txt file
pybank_output = open("pybank.txt", "w")

print("financial analysis", file=pybank_output)
print(f"total months: {len(dates)}", file=pybank_output)
print(f"total: ${total}", file=pybank_output)
print(f"average change: ${avg_change}", file=pybank_output)
print(f"Greatest increase in profits: ${max_val} on {dates[max_ind]}", file=pybank_output)
print(f"Greatest decrease in profits: ${min_val} on {dates[min_ind]}", file=pybank_output)

#pybank_output.writelines(L)
pybank_output.close()

#moves .txt file to analysis folder
shutil.move("pybank.txt", "analysis" )