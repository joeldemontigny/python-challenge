import os
import csv

budget_csv = os.path.join(".","Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    totals = []
    changes=[]
    change=0
    months=[]
    for row_count, row in enumerate(csvreader, start=1):
        value = int(row['Profit/Losses'])
        totals.append(value)
        changes.append(value-change)
        months.append(row['Date'])
        change= value

   

Max= (max(changes))
maxIndex =changes.index(Max)
maxMonth=months[maxIndex]

Min= (min(changes))
minIndex =changes.index(Min)
minMonth=months[minIndex]

averageChanges= sum(changes)/len(changes)

print ("Financial Analysis")
print ("-------------------------------")
print ("Total Months: {}".format(row_count))
print ("Total: ${}".format(sum(totals)))
print ("Average Change: $", int(averageChanges))
print(f'Greatest Increase in Profits: {maxMonth} (${Max})')
print (f"Greatest Decrease in Profits: {minMonth} (${Min})")


output_file = os.path.join("Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    text_file.write ("Financial Analysis\n")
    text_file.write ("-------------------------------\n")
    text_file.write ("Total Months: {}\n".format(row_count))
    text_file.write ("Total: {}\n".format(row_count))
    text_file.write ("Average Change: ${}\n".format((averageChanges)))
    text_file.write (f'Greatest Increase in Profits: {maxMonth} (${Max})\n')
    text_file.write (f"Greatest Decrease in Profits: {minMonth} (${Min})")