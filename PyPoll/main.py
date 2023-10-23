#importing what we will need.
import os
import csv
import numpy as np

#reading the file provided.
poll_csv = os.path.join("Resources", "election_data.csv")

#opening the file that was privided.
with open(poll_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    #making sure the the header doesn't mess up my code
    next(csvreader)

    #creating the list to hold the rows I will need.
    ballot_ID = []
    candidate = []

    #adding the elements for the rows.
    for row in csvreader:
        ballot_ID.append(row[0])
        candidate.append(row[2])

    #finding the unique candidates in this file. I did print this off to see how many there were, which was 3.
    person = np.unique(candidate)
    #storing each candidate.
    p1 = person[0]
    p2 = person[1]
    p3 = person[2]

    #counting the number of votes for each candiate.
    cand1 = candidate.count(p1)
    cand2 = candidate.count(p2)
    cand3 = candidate.count(p3)
        
    #figuring out the number of total votes
    total_votes = len(ballot_ID)

    #figuring out the percentage of votes for each candidate.
    percent1=(cand1/total_votes)*100
    percent2=(cand2/total_votes)*100
    percent3=(cand3/total_votes)*100

    #figuring out the winner
    candlist = max(cand1,cand2,cand3)
    if candlist == cand1:
        winner = p1
    elif candlist == cand2:
        winner = p2
    elif candlist == cand3:
        winner = p3

    #printing the results
    print("Election Results\n")
    print("-------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print(f"{p1}: {round(percent1,3)}% ({cand1})\n")
    print(f"{p2}: {round(percent2,3)}% ({cand2})\n")
    print(f"{p3}: {round(percent3,3)}% ({cand3})\n")
    print("-------------------------\n")
    print(f" Winner: {winner}\n")
    print("-------------------------\n")

    #writing the results as a file as well.
    file = open("analysis\Export.txt","w")
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"{p1}: {round(percent1,3)}% ({cand1})\n")
    file.write(f"{p2}: {round(percent2,3)}% ({cand2})\n")
    file.write(f"{p3}: {round(percent3,3)}% ({cand3})\n")
    file.write("-------------------------\n")
    file.write(f" Winner: {winner}\n")
    file.write("-------------------------\n")
    file.close