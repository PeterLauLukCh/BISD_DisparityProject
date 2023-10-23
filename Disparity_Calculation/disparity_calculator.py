import os
import csv

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'Names_2010Census.csv')
frequency = []
race_probabilities = []
race = ["White","Black","API","AIAN","2prace","Hispanic"]

with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    
    for row in csvreader:
        if(row[0] == 'name'):
            continue
        frequency.append(int(row[2]))
        probabilities_row = []
        for i in range(5, 11):  
            value = row[i]
            if value and value != '(S)':
                probabilities_row.append(float(value) / 100)
            else:
                probabilities_row.append(0)
        race_probabilities.append(probabilities_row)

results = []
for i in range(6):
    result = sum(frequency[j] * race_probabilities[j][i] for j in range(len(frequency)))
    results.append(result)

current_directory = os.path.dirname(__file__)
output_file_path = os.path.join(current_directory, 'Disparity_Output.txt')
with open(output_file_path, 'w') as file:
    for i in range(6):
        line = f"{race[i]} {results[i]}\n"
        file.write(line)
for i in range(6):
    print(race[i],results[i])
print(f"Results have been written to: {output_file_path}")
