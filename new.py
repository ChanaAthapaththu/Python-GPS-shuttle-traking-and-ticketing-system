import csv
import sys
import numpy as np 

#input number you want to search
number = input('Enter number to find\n')

#read csv, and split on "," the line
with open('mycsv.csv', newline='') as csvfile:
  

# for line in csv_file:
#loop through csv list
  for row in csvfile:
     if number == row[0]:
        print(row)
        print(row[0])
        print(row[11:19])
        print(row[21:30])
        break
        
           
       
         
         

         