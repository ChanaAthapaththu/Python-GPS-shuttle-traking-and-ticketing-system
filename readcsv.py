import csv

with open('mycsv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    RFIDs = []
    dates = []
    inlats = []
    inlngs = []
    for row in readCSV:
        RFID = row[0]
        date = row[1]
        inlat = row[2]
        inlng = row[3]
        

        RFIDs.append(RFID)
        dates.append(date)
        inlats.append(inlat)
        inlngs.append(inlng)


       
        
       

    print(RFID)
    print(date)
    print(inlat)
    print(inlng)
    