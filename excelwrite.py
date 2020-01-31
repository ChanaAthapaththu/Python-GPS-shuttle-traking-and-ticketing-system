# import xlsxwriter module 
import xlsxwriter 
  
workbook = xlsxwriter.Workbook('Example3.xlsx') 
# Take inputs
a=input('Enter the RFID number: ')
b=input('Enter InTime: ')
c=input('Enter InLng: ')
d=input('Enter InLat: ')
  
# By default worksheet names in the spreadsheet will be  
# Sheet1, Sheet2 etc., but we can also specify a name. 
worksheet = workbook.add_worksheet("My sheet") 
  
# Some data we want to write to the worksheet. 
scores = ( 
    [a, b,c,d], 
     ) 
  
# Start from the first cell. Rows and 
# columns are zero indexed. 
row = 0
col = 0
  
# Iterate over the data and write it out row by row. 
for a, b,c,d in (scores): 
    worksheet.write(row, col, a) 
    worksheet.write(row, col + 1, b) 
    worksheet.write(row, col + 2, c)
    worksheet.write(row, col + 3, d)
    row += 1
  
workbook.close() 