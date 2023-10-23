"""
This module includes a program that reads data from 'Names_2010Census.csv' 
and calculates the estimated number of voters from different races using the frequency
and probability data from 'Names_2010Census.csv'. 

Functions
---------
Data_Path_Set:
    Retrieves the path of 'Names_2010Census.csv'
Read_In:
    Reads data from the CSV file and stores it in arrays
Calculation:
    Calculates the estimated number of voters in different races
Write_Out:
    Prints the result and writes it to a file 
"""
import csv
import os

"""
Initializing arrays to store data read from 'Names_2010Census.csv'.
'Names_2010Census.csv' contains 162,254 surnames. 

Parameters:
frequency: 1D array to store the frequency of surname y_{i}; size: 1x162,254 
race_probabilities: 2D array to store the probabilities of y_{i} belonging to different races; size: 6x162,254
race: 1D array to store the races; size: 1x6
results: 1D array to store the estimated number of voters in 6 races; size 1x6
"""
frequency = []
race_probabilities = []
race = ["White", "Black", "API", "AIAN", "2prace", "Hispanic"]
results = []

# Returns the path of 'Names_2010Census.csv' on the machine
def Data_Path_Set():
    current_directory = os.path.dirname(__file__)
    return os.path.join(current_directory, 'Names_2010Census.csv')

# Opens 'Names_2010Census.csv'; reads and stores column C, column F to K
def Read_In():
    file_path = Data_Path_Set()
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        
        for row in csvreader:
            # Skips the first row of the table
            if row[0] == 'name':
                continue

            # Appends the frequency of surname y_{i} to the array
            frequency.append(int(row[2]))
            probabilities_row = []

            # Appends the probabilities of surname y_{i} to the array
            for i in range(5, 11):  
                value = row[i]
                if value and value != '(S)':
                    probabilities_row.append(float(value) / 100)
                else:
                    # If the probability y_{i} belongs to a certain race is 0
                    probabilities_row.append(0)
                
            race_probabilities.append(probabilities_row)

# Calculates the estimated number of voters in 6 races using the formula derived in README.md
def Calculation():
    for i in range(6):
        # Num of Voters in Race_{i} = \sum_{i=1}^{162254} frequency_{y_{i}} * Pr(y{i} is Race_{i})
        result = sum(frequency[j] * race_probabilities[j][i] for j in range(len(frequency)))
        results.append(result)

# Prints the result and writes it to a file
def Write_Out():
    current_directory = os.path.dirname(__file__)
    output_file_path = os.path.join(current_directory, 'Disparity_Output.txt')

    with open(output_file_path, 'w') as file:
        for i in range(6):
            line = f"{race[i]} {results[i]}\n"
            file.write(line)
            
    for i in range(6):
        print(race[i], results[i])
        
    # Shows the path to find the result file
    print(f"Results have been written to: {output_file_path}")

def Main():
    Data_Path_Set()
    Read_In()
    Calculation()
    Write_Out()

Main()
