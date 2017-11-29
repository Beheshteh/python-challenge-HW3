
#
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to the one below:
#
#Election Results
#-------------------------
#Total Votes: 620100
#-------------------------
#Rogers: 36.0% (223236)
#Gomez: 54.0% (334854)
#Brentwood: 4.0% (24804)
#Higgins: 6.0% (37206)
#-------------------------
#Winner: Gomez
#-------------------------
#Your final script must be able to handle any such similarly-structured dataset in 
#the future (i.e you have zero intentions of living in this hillbilly town -- so your
# script needs to work without massive re-writes). In addition, your final script
#should both print the analysis to the terminal and export a text file with the results.

import os
import csv

morerecord = "y"

while morerecord == "y":

    candidatelist = []     #Save the name of candidate
    allVoteList = []       #Save all the list of all vote
    numVote = []           #Save the number of vote for each candidate
    totalVote = 0
    firstVote = "y"
    
    FileName = input("Which poll do you want to analyze?"
     +" (Please provide the name of .csv file with special structure)\n")

    #Open and read csv
    with open(FileName +'.csv', newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #Skip the header
        next(csvreader,None)
        for row in csvreader:
            newCand = 1
            totalVote = totalVote + 1
            allVoteList.append(row[2])

            if firstVote == "y":
                candidatelist.append(row[2])
                firstVote = "n"
                                
            else:
                #check for the new name for candidate
                for i in range(len(candidatelist)):
                    if candidatelist[i] == row[2]:
                        newCand = 0
                        break
                    else:
                        i = i + 1    
                       
                if newCand == 1:
                    candidatelist.append(row[2])
                        
                        
    # Time to print the result                                          
                           
    print("             Election Results                \n")
    print("\n--------------------------------------------\n")
    print("Total Votes: " + str(totalVote))
    print("\n--------------------------------------------\n")

    # Save the result in the file
    outfile = open('analyzed_'+ FileName, 'w')
    outfile.write("\n           Election Results                \n")
    outfile.write("\n-------------------------------------------\n")
    outfile.write("Total Votes: " + str(totalVote))
    outfile.write("\n--------------------------------------------\n")


    for i in range(len(candidatelist)):
        numVote.append(allVoteList.count(candidatelist[i]))
        percentVote = round(float(numVote[i]) / totalVote, 2)
        print(candidatelist[i] + ":" + str(percentVote) + "%  (" + str(numVote[i]) + ") \n")
        # Save the result in the file
        outfile.write(candidatelist[i] + ":" + str(percentVote) + "%  (" + str(numVote[i]) + ") \n")

    print("\n--------------------------------------------\n")    

    maxVote = numVote.index(max(numVote))
    winCandidate = candidatelist[maxVote]
    print("Winner: " + str(winCandidate))
    print("\n--------------------------------------------\n")

     # Save the result in the file
    outfile.write("\n--------------------------------------------\n")    
    outfile.write("Winner: " + str(winCandidate))
    outfile.write("\n--------------------------------------------\n")

    outfile.close()
    
    morerecord = input("Do you want to analyze more record? (y/n)")
    
    
    

    

    
        

    