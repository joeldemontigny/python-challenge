import os
import csv
title = "Financial Analysis"
spacer = "---------------------------------"
csvpath = os.path.join(".","Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    header=next(csvreader)
    months =[]
    for row in csvreader:
        if row[0] not in months:
            months.append(row[0])

    sum = 0
   
    print (title) 
    print (spacer)   
    print("Total Months:", len(months))
    #print("Total:", sum(totalprofit))
    #print("Average Change:", mean(change))
    #print("Greatest Increase in Profit:", max(increase))
    #print("Greatest Decrease in Profit:", min(decrease))


# Need to skip the header

#Sum the total number of months
# months = array value 0 


# totalMonths = len(months)
