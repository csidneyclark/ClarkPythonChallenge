import os
import csv
import statistics
#locate file with data
file = os.path.join("election_data.csv")

#declare variables
total_voterid = 0
unique_list = []
Khan = 0
Correy = 0
Li = 0
OTooley = 0


#open file and read data with csv.reader
with open(file) as data: 
    csvreader = csv.reader(data, delimiter = ',')
    header = next(csvreader)

    candidates = {}
    #loop through csv data
    for row in csvreader:
        #The total number of votes cast
        total_voterid += 1
        #A complete list of candidates who received votes
        if row [2] not in unique_list:
            unique_list.append(row[2])
        #Khan's total votes
        if row[2] == "Khan": 
            Khan += 1
        #Correy's total votes
        if row[2] == "Correy":
            Correy += 1
        #Li's total votes
        if row[2] == "Li":
            Li += 1
        #O'Tooley's total votes
        if row[2] == "O'Tooley":
            OTooley += 1
        #calculating winner based on popular vote
        winning_votes = 0
        winner = ""
    if Khan >= winning_votes:
        winning_votes = Khan
        winner = "Khan"
    if Correy > winning_votes:
        winning_votes = Correy
        winner = "Correy"
    if Li > winning_votes:
        winning_votes = Li
        winner = "Li"
    if OTooley > winning_votes:
        winning_votes = OTooley
        winner = "O'Tooley"
        
    #Khan's percentage of votes
    khan_percentage = round((Khan / total_voterid)*100, 3)
    #Correy's percentage of votes
    correy_percentage = round((Correy / total_voterid)*100, 3)
    #Li's percentage of votes
    li_percentage = round((Li / total_voterid)*100, 3)
    #O'Tooley's percentage of votes
    otooley_percentage = round((OTooley/ total_voterid)*100, 3)


analysis = f"""
Election Results
-----------------
Total Number of Votes Cast: {total_voterid}
Candidates: {unique_list}
Khan: {khan_percentage}%, {(Khan)} total votes
Correy: {correy_percentage}%, {(Correy)} total votes
Li: {li_percentage}%, {Li} total votes
O'Tooley: {otooley_percentage}%, {OTooley} total votes
Winner: {winner}
"""
print(analysis)

file = open("PyPolloutput.txt", "w")
file.write(analysis)
file.close()

