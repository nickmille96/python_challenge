import csv, os

file_load="resources/budget_data.csv"
file_output="analysis/budget_output.csv"

totalmonths=0
totalnet=0

with open (file_load) as file:
    reader=csv.reader(file)
    header=next(reader)
    print (header)
    firstrow=next(reader)
    
    totalmonths += 1
    totalnet += int(firstrow[1])
    previousnet=int(firstrow[1])
    for row in reader:
        totalmonths += 1
        totalnet += int(firstrow[1])

        