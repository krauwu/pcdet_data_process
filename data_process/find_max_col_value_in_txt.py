import csv

max_value = float('-inf')
with open('1.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        value = list(map(float, row[0].split()))[1]
        if value > max_value:
            max_value = value

print('The maximum value in the second column is:', max_value)
