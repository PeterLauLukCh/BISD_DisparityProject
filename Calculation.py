import csv
frequency = []
race_probabilities = []
race = ["White","Black","API","AIAN","2prace","Hispanic"]

with open('/Users/chenpeter/Downloads/Names_2010Census.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)

    for row in csvreader:
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

for i in range(6):
    print(race[i],results[i])
