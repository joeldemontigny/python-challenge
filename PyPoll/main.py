#main.py
import os
import csv

#create path to file

electiondatapath = os.path.join('.','Resources', 'election_data.csv')

#Open csv file, skip headers, and define variables

with open (electiondatapath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    num_rows = 0
    totalvotesDic = {}
    results = []

#identify vote count per candidate and progression to next candidate
    for row in csvreader:

        num_rows += 1
        if row[2] not in totalvotesDic.keys():
            totalvotesDic[row[2]] = 1
        else:
            totalvotesDic[row[2]] += 1

#Print output of desired data in terminal

print("Election Results")
print("-----------------------")
print(f"Total Votes: {(num_rows)}")
print("-----------------------")

#specify output of variables to 3 decimal points and required calculation for desired outcome
for candidates in totalvotesDic.keys():
    
    candidates_info = candidates, "{:.3%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")"
    print(candidates, "{:.3%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")")

winner = max(totalvotesDic, key=totalvotesDic.get)

#Print output of desired data in terminal

print("-----------------------")
print(f"Winner: {(winner)}")
print("-----------------------")

results.append("Election Results")
results.append(f"Total Votes: {(num_rows)}")
results.append(candidates_info)
results.append(f"Winner: {(winner)}")


cleaned_csv = zip(results)

#Create output file

output_file = os.path.join("Analysis.txt")

#Open the output file

with open(output_file, "w") as text_file:
    text_file.write (f"Election Results\n")
    text_file.write ("-------------------------------\n")
    text_file.write (f"Total Votes: {(num_rows)}\n")
    text_file.write ("-----------------------\n")
    for candidates in totalvotesDic.keys():
        candidates_info = candidates, "{:.3%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")"
        string=candidates + " " +  str("{:.3%}".format(totalvotesDic[candidates] / num_rows) + " (" + str(totalvotesDic[candidates])+ ")\n")
        text_file.write(string)
    
    text_file.write ("-----------------------\n")

    text_file.write (f"Winner: {(winner)}\n")
    text_file.write ("-----------------------")
