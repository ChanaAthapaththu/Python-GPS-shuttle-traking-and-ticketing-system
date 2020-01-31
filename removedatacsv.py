import csv
lines = list()

members= input("Please enter a member's name to be deleted.")

with open('mycsv.csv', 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if field == members:

                lines.remove(row)

with open('mycsv.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)