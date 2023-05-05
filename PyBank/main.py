import os
import csv

#create path to file

budget_csv = os.path.join(".","Resources", "budget_data.csv")

#Open csv file, skip headers, and define variables

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    changes=[]
    change=0
    months=[]

#define additional values and identify columns
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        totals.append(value)
        changes.append(value-change)
        months.append(row['Date'])
        change= value

#Additional value calculation, max, min, average  

Max= (max(changes))
maxIndex =changes.index(Max)
maxMonth=months[maxIndex]

Min= (min(changes))
minIndex =changes.index(Min)
minMonth=months[minIndex]

averageChanges= round(sum(changes[1:])/len(changes[1:]),2)

#Print output of desired data in terminal

print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: ${}".format(sum(totals)))
print ("Average Change: $",(averageChanges))
print(f'Greatest Increase in Profits: {maxMonth} (${Max})')
print (f"Greatest Decrease in Profits: {minMonth} (${Min})")

#Create output file

output_file = os.path.join("Analysis.txt")

#Open the output file
with open(output_file, "w") as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("-------------------------------\n")
    text_file.write ("Total Months: {}\n".format(row_count))
    text_file.write ("Total: {}\n".format(row_count))
    text_file.write ("Average Change: ${}\n".format((averageChanges)))
    text_file.write (f'Greatest Increase in Profits: {maxMonth} (${Max})\n')
    text_file.write (f"Greatest Decrease in Profits: {minMonth} (${Min})")