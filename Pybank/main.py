#-----------------------------------------------------
#In this challenge you are tasked with creating a Python script for analyzing the financial 
#records of your company. You will be given two sets of revenue data (budget_data_1.csv and 
#budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue.
#
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:
#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)

#--------------------------------------------------------
#Your final script must be able to handle any such similarly structured
# dataset inthe future (your boss is going to give you more of these --
# so your script has to work for the ones to come). In addition,
# your final script should both print the analysis 
#to the terminal and export a text file with the results.


import os
import csv


morerecord = "y"

while morerecord == "y":

    Datelist = []
    revenuelist = []
    AllRevenueChange = []
    countData = 0
    totalRevenue = 0

    FileName = input("Which record do you want to analyze?"
     +" (Please provide the name of .csv file with special structure)")

    #Open and read csv
    with open(FileName +'.csv', newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        #Skip the header
        next(csvreader,None)
        for row in csvreader:
            countData = countData +1
            Datelist.append(row[0])
            totalRevenue = totalRevenue + float(row[1])
            revenuelist.append(row[1])
                  
    for i in range(len(revenuelist)-1):
        revenueChange = float(revenuelist[i+1])- float(revenuelist[i])
        AllRevenueChange.append(revenueChange)
    
    AverevenueChange = sum(AllRevenueChange) / float(len(AllRevenueChange))
    MaxrevenueChange = max(AllRevenueChange)
    Maxindex = AllRevenueChange.index(MaxrevenueChange)
    MinrevenueChange = min(AllRevenueChange)
    Minindex = AllRevenueChange.index(MinrevenueChange)
    
    # Print output in the screen
    print("\n--------------------------------------------------------------\n")
    print("Total Months: " + str(countData))
    print("Total Revenue: " + str(totalRevenue))
    print("Average Revenue Change: " + str(AverevenueChange))
    print("Greatest Increase in Revenue: " + str(Datelist[Maxindex]) +"   " + str(MaxrevenueChange))
    print("Greatest Decrease in Revenue: " + str(Datelist[Minindex]) +"   " + str(MinrevenueChange))
        
    # save the output in the file
    outfile = open('analyzed_'+ FileName, 'w')
    outfile.write("\n Total Months: " + str(countData) + "\n")
    outfile.write("Total Revenue: " + str(totalRevenue) + "\n")
    outfile.write("Average Revenue Change: " + str(AverevenueChange) + "\n")
    outfile.write("Greatest Increase in Revenue: " + str(Datelist[Maxindex]) +
    "   " + str(MaxrevenueChange) + "\n")
    outfile.write("Greatest Decrease in Revenue: " + str(Datelist[Minindex]) +
    "   " + str(MinrevenueChange) + "\n")
    outfile.close()
    
    morerecord = input("Do you want to analyze more record? (y/n)")