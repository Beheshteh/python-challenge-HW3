#-----------------------------------------------------
#Your task is to help bridge the gap by creating a Python script able
# to convert your employee records to the required format. Your script
# will need to do the following:

#-------------------------------------------------------------------
#Import the employee_data1.csv and employee_data2.csv files,
# which currently holds employee records like the below:
#
#Emp ID,Name,DOB,SSN,State
#214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#15,Samantha Lara,1993-09-08,848-80-7526,Colorado
#
#Then convert and export the data to use the following format instead:
#
#Emp ID,First Name,Last Name,DOB,SSN,State
#214,Sarah,Simpson,12/04/1985,***-**-8166,FL
#15,Samantha,Lara,09/08/1993,***-**-7526,CO
#
#----------------------------------------------------------------------
#In summary, the required conversions are as follows:
#The Name column should be split into separate First Name and Last
# Name columns.
#The DOB data should be re-written into DD/MM/YYYY format.
#The SSN data should be re-written such that the first five numbers 
#are hidden from view.
#The State data should be re-written as simple two-letter abbreviations.
#Special Hint: You may find this link to be helpful—Python Dictionary 
#for State Abbreviations.

import os
import csv
from datetime import datetime
import datetime

# use this dictionary to convert the full name of each state to its abbreviation
states = {
        'Alabama':'AL',
        'Alaska':'AK',
        'Arizona':'AZ',
        'Arkansas':'AR',
        'California':'CA',
        'Colorado':'CO',
        'Connecticut':'CT',
        'Delaware':'DE',
        'Florida':'FL',
        'Georgia':'GA',
        'Hawaii':'HI',
        'Idaho':'ID',
        'Illinois':'IL',
        'Indiana':'IN',
        'Iowa':'IA',
        'Kansas':'KS',
        'Kentucky':'KY',
        'Louisiana':'LA',
        'Maine':'ME',
        'Maryland':'MD',
        'Massachusetts':'MA',
        'Michigan':'MI',
        'Minnesota':'MN',
        'Mississippi':'MS',
        'Missouri':'MO',
        'Montana':'MT',
        'Nebraska':'NE',
        'Nevada':'NV',
        'New Hampshire':'NH',
        'New Jersey':'NJ',
        'New Mexico':'NM',
        'New York':'NY',
        'North Carolina':'NC',
        'North Dakota':'ND',
        'Ohio':'OH',
        'Oklahoma':'OK',
        'Oregon':'OR',
        'Pennsylvania':'PA',
        'Rhode Island':'RI',
        'South Carolina':'SC',
        'South Dakota':'SD',
        'Tennessee':'TN',
        'Texas':'TX',
        'Utah':'UT',
        'Vermont':'VT',
        'Virginia':'VA',
        'Washington':'WA',
        'West Virginia':'WV',
        'Wisconsin':'WI',
        'Wyoming':'WY'
}

# create the list of data file to read from
FileName =['employee_data1.csv', 'employee_data2.csv']

# for all the file in the data file list clean the data and write the new data in the new file
for i in range(len(FileName)):

    # for each file in the data file list define new set of variable
    EmID =[]
    FirstName = []
    LastName = []
    DOB = []
    SSN =[]
    StateabbName =[]
    infolist = []
    firstLine = "yes"
    
    # Read from each file in the list 
    with open(FileName[i], newline="") as infile:
        csvreader = csv.reader(infile, delimiter=",")
        
        #Skip the header
        next(csvreader,None)
        for row in csvreader:
            # clean each row of data from csv file based on the requirment
            EmID.append(row[0])
            Name = row[1].split(" ")
            FirstName.append(Name[0])
            LastName.append(Name[1])
            Date = row[2]
            DOB.append(datetime.datetime.strptime(Date, '%Y-%m-%d').strftime('%m/%d/%Y'))
            Socialcode = row[3].split('-')
            SSN.append("***-**-" + Socialcode[2])
            statefull = row[4]
            StateabbName.append(states[statefull])
   

    # combined all the cleaned data in the new list    
    cleaned_csv = zip(EmID, FirstName, LastName, DOB, SSN, StateabbName)

    # write the cleaned data in the new file
    with open('new_'+ FileName[i] , 'w',newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Emp ID', 'First name', 'last name', 'DOB', 'SSN', 'State'])
        writer.writerows(cleaned_csv)

    outfile.close( )    


