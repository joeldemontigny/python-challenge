import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    header=next(csvreader)
    print(header)

# Need to skip the header

#Sum the total number of months
# months = array value 0 


# totalMonths = len(months)
