# Import modules
import os
import csv

csvpath = os.path.join('raw_data', 'budget_data_1.csv')

total = 0
change = 0
revTotal = []
difference = []
# Open file wiht raw data
with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Omit header row
    next(csvreader, None)

    # data = list(csvreader)
    
    # # Count of rows
    # rows = len(data)
    # print(rows)

    for row in csvreader:

        # Running total of revenue
        total = total + float(row[1])
        revTotal.append(total)
        print(total)

        # Change in monthly revenue
        if float(row[1]-1) is float:
            change = float(row[1]) - float(row[1]-1)
            difference.append(change)