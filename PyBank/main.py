import csv, os



total=0 
profitloss=0 
value=0
monthchange=0 
profits=[]
dates= []

file_load= os.path.join("budget_data.csv")
file_output=os.path.join("outputPyBank.csv")

with open (file_load) as file:
    reader=csv.reader(file)
    header=next(reader)
    print (header)

    for row in reader:
        #dates
        dates.append(row[0])
        firstrow = next(reader)
        profitloss += int(firstrow[1])
        total += 1
        value =int(firstrow[1])

        #calculate month change
        monthchange= int(row[1])-value
        profits.append(monthchange)
        value =int(row[1])
        total += 1

        #change in profit and loss
        profitloss= profitloss +int(row[1])

    #increace in profits
    profitincrease= max(profits)
    greatestindex= profits.index(profitincrease)
    greatestdate= dates[greatestindex]

    #decreace in profits
    greatestdecrease= min(profits)
    lowestindex= profits.index(greatestdecrease)
    lowestdate= dates[lowestindex]

    #calculate average change
    averagechange=sum(profits)/len(profits)
#print
print("Financial Analysis")
print("---------------")
print(f"TotalMonths:{str(total)}")
print(f"Total: {str(profitloss)}")
print(f"Average Change: ${averagechange}")
print (f"Greatest Increase in Profits: ({greatestdate}(${profitincrease})")
print(f"Greatest Decrease in Profits: ({lowestdate}(${greatestdecrease})")

#output
with open(file_output, "w") as text:
    text.write(f"Financial Analysis\n")
    text.write(f"---------------------\n")
    text.write(f"Total Months: {total}\n")
    text.write(f"Total: ${profitloss}\n")
    text.write(f"Average Change: ${averagechange}\n")
    text.write(f"Greatest Increase in Profits: {greatestdate}(${profitincrease})")
    text.write(f"Greatest Decrease in Profits:{lowestdate}(${greatestdecrease})")