import csv, os

file_load=("election_data.csv")
file_output=("outputPypoll.csv")


totalvotes= 0
winnercount= 0
#Vote count by candidate
votecount= []
percentagevote =[]
canidates=[]

#Loop through reader 
with open (file_load) as file:
    reader=csv.reader(file)
    header=next(reader)
    print (header)

    for row in reader:
        totalvotes +=1

#If canidate is not on list add them. Then add votes 
        if row [2] not in canidates:
            canidates.append(row[2])
            index=canidates.index(row[2])
            votecount.append(1)
        else:
            index=canidates.index(row[2])
            votecount[index] +=1
            

    for votes in votecount:
#vote percentage 
        votepercent= (votes/totalvotes) *100
        votepercent= round(votepercent)
        percentagevote.append(votepercent)
        

#Find the winner 

    winner= max(votecount)
    index=votecount.index(winner)
    electionwinner= canidates[index]

#print results 

print(f"Election Results\n")
print(f"Total Votes: {str(totalvotes)}")
for i in range(len(canidates)):
    print(f"{canidates[i]}:{str(percentagevote[i])}({str(votecount[i])})")

print(f"---------------------")
print(f"Winner:{electionwinner}")

#output 
with open(file_output, "w") as text:
    text.write(f"Election Results\n")
    text.write(f"Total Votes: {str(totalvotes)}")
    for i in range(len(canidates)):
        text.write(f"{canidates[i]}:{str(percentagevote[i])}({str(votecount[i])})")
    text.write(f"---------------------")
    text.write(f"Winner:{electionwinner}")


    


    