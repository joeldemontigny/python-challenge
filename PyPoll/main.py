#main.py
import os
import csv

electiondatapath = os.path.join('.','Resources', 'election_data.csv')


with open (electiondatapath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    num_rows = 0
    totalvotesDic = {}
    results = []


    for row in csvreader:

        num_rows += 1
        if row[2] not in totalvotesDic.keys():
            totalvotesDic[row[2]] = 1
        else:
            totalvotesDic[row[2]] += 1

print("Election Results")
print("-----------------------")
print(f"Total Votes: {(num_rows)}")
print("-----------------------")


for candidates in totalvotesDic.keys():
    
    candidates_info = candidates, "{:.3%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")"
    print(candidates, "{:.3%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")")

winner = max(totalvotesDic, key=totalvotesDic.get)

print("-----------------------")
print(f"Winner: {(winner)}")
print("-----------------------")

results.append("Election Results")
results.append(f"Total Votes: {(num_rows)}")
results.append(candidates_info)
results.append(f"Winner: {(winner)}")


cleaned_csv = zip(results)

output_file = os.path.join("Analysis.txt")


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
