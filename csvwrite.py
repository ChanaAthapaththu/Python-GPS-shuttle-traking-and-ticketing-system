import csv
# Take inputs
a=input('Enter the RFID number: ')
b=input('Enter InTime: ')
c=input('Enter InLng: ')
d=input('Enter InLat: ')

with open('mycsv.csv','w',newline='') as f: 
    thewriter = csv.writer(f)
    thewriter.writerow([a,b,c,d])
    # thewriter.writerow(['one','two','three'])     
