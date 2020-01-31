import csv
import sys

number=input("Enter nu")
with open('mycsv.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # print(row)
        if number==row[0]:
          print(row)
