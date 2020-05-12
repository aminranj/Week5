import csv

with open('person.csv') as csvFile:
    r = csv.reader(csvFile)
    for row in r:
        print(row[1])
