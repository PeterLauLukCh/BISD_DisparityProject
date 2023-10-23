"""
This module includes the program that reads the data from 'Names_2010Census.csv' 
and calculate the estimated number of voters from different races using the frequency
and probability from 'Names_2010Census.csv'. 

Functions
---------
Data_Path_Set
    retrive the path of 'Names_2010Census.csv'
Read_In
    read in the data from csv and stores them to the array
Calculation
    calculate the estimated number of voters in different races
Write_Out
    print the result and write out a file 
"""
import csv
import os

"""
Initializing the arrays to store the data read from 'Names_2010Census.csv'.
'Names_2010Census.csv' contains 162254 surnames. 

Parameters:
frequency: 1D array to store the frequency of surname y_{i}; size: 1x162254 
race_probabilities: 2D array to store the probabilities of y_{i} belonging to different races; size: 6x162254
race: 1D array to store the races; size: 1x6
results: 1D array to store the estimated number of voters in 6 races; size 1x6
"""
frequency = []
race_probabilities = []
race = ["White","Black","API","AIAN","2prace","Hispanic"]
results = []

#return the path of 'Names_2010Census.csv' in machine
def Data_Path_Set():
    current_directory = os.path.dirname(__file__)
    return os.path.join(current_directory, 'Names_2010Census.csv')

#open 'Names_2010Census.csv'; read and stores column C, column F to K
def Read_In():
    file_path = Data_Path_Set()
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        
        for row in csvreader:
            #neglect the first row of the table
            if(row[0] == 'name'):
                continue

            #append the frequency of surname y_{i} to array
            frequency.append(int(row[2]))
            probabilities_row = []

            #append the probabilities of surname y_{i} to array
            for i in range(5, 11):  
                value = row[i]
                if value and value != '(S)':
                    probabilities_row.append(float(value) / 100)
                else:
                    #if the probability y_{i} belongs to certain race is 0
                    probabilities_row.append(0)
                
            race_probabilities.append(probabilities_row)

def Calculation():
    for i in range(6):
        result = sum(frequency[j] * race_probabilities[j][i] for j in range(len(frequency)))
        results.append(result)

def Write_Out():
    current_directory = os.path.dirname(__file__)
    output_file_path = os.path.join(current_directory, 'Disparity_Output.txt')

    with open(output_file_path, 'w') as file:
        for i in range(6):
            line = f"{race[i]} {results[i]}\n"
            file.write(line)
            
    for i in range(6):
        print(race[i],results[i])
        
    print(f"Results have been written to: {output_file_path}")

def Main():
    Data_Path_Set()
    Read_In()
    Calculation()
    Write_Out()

Main()
