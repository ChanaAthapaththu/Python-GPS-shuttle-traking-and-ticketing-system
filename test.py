import time
import requests
import json
import googlemaps 
import mysql.connector
from datetime import date
from datetime import datetime

# Database connection
mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="rfiddata")
mycursor=mydb.cursor()


#Fetch data from SLIIT shuttle GPS API
pload = { 'Origin':'https://esfm.dialog.lk',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept':'*/*',}


r = requests.post('https://esfm.dialog.lk/api-v2/tracker/get_states',data = 'hash=8b64f84b0b87681b0ac92a81a565670b&list_blocked=true&trackers=%5B473754%2C473755%2C473757%2C473758%5D',headers=pload)


j = r.json()
location=j['states']['473758']['gps']['location']
latitude=j['states']['473758']['gps']['location']['lat']
longitude=j['states']['473758']['gps']['location']['lng']
movement_status=j['states']['473758']['movement_status']

#_______________________________________________________________________________________________________________________________


#Validate user and verify the card status and other calculations

x=input('\n Please Tap your ID Card !!! ')

with open('sample.txt') as f:
    if x in f.read():
        print("###########-------------------((OUT))----------------------############")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        
        print("Metro Shuttle")
        print("==============")
        print("Out Time",current_time)
       
        
        print ("Out Latitude : ",latitude)
        print ("Out Longitude : ",longitude)
        print ("Out Status: "+movement_status)
        number=x
        # print("Your Records are Removed")
        # #Read amd take the highest id
        # sqlx=("SELECT MAX(data_id) FROM devicedata where rfid =%s")
        # valx=(number)
        # mycursor.execute(sqlx,(valx,))
        # myresultx = mycursor.fetchall()
        # for x in myresultx:
        #     dataidMax=x[0]
        # print(myresultx)
            

        # Read data from db
       
        sql1 = ("SELECT timein,latin,lngin FROM devicedata where rfid =%s ")
        val1=(number)
        mycursor.execute(sql1,(val1,))
        myresult = mycursor.fetchall()

        # specifing the data from the database file
        for y in myresult:  
         time1=y[0]
         lat1=y[1]
         lng1=y[2]
         
        
         location1=lat1,lng1
         location2=latitude,longitude

        # Calculating the travelled time
        s2=current_time
        s1=time1
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
        

        print("Toatal Time Travelled: ",tdelta)
       
             #  API key 
        gmaps = googlemaps.Client(key='') 
                
             # calculating the distance 
        my_dist = gmaps.distance_matrix(location1,location2)['rows'][0]['elements'][0] 
                
             # Printing the result 
         
        distance= my_dist['distance']['text']
        print('Total Diatance Travelled: ',distance)
        # Calculating the bus fee

        rate=float(1.5000)
        if (distance.find('km') != -1):
            q=float(distance.replace('km',''))
            busfee=q*rate
            print("Bus Fare:Rs",busfee)
        
        
        else: 
            q=float(distance.replace('m',''))
            busfee=rate*q/float(1000)
            print("Bus Fare:Rs",busfee)

        #update the data with  the exit values

        sql2= ("UPDATE devicedata SET timeout = %s,latout = %s,lngout = %s,timetraveled = %s,distancetraveled = %s, travelfee= %s WHERE rfid = %s And timein=%s ;")

        val2=(current_time,latitude,longitude,tdelta,distance,busfee,x,time1)
        mycursor.execute(sql2,val2)
        mydb.commit()


        print(mycursor.rowcount, "record inserted.")
       
        
        # Remove user from text file
        with open("sample.txt", "r") as f:
         lines = f.readlines()
        with open("sample.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != x:
                    f.write(line)

                   
        

    else: 
        print("#############-------------------((IN))----------------------###############")
        print("Welcome To SLIIT Shuttle Service")
        print("================================")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
       
        print("Metro Shuttle")
        print("IN time:",current_time)
        today = date.today()
        print("Today's date:", today)
       
        # print ("Out Latitude : ",location)
       
        print ("In Latitude : ",latitude)
        print ("In Longitude : ",longitude)
        print ("Movement Status: "+movement_status)

        # write IN data to database  
            
        sql = "INSERT INTO devicedata (rfid,date,timein,latin,lngin,timeout,latout,lngout,timetraveled,distancetraveled,travelfee) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
        val = (x, today, current_time, latitude, longitude, "", 0.0, 0.0, "", "","")
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

                

        # writing RFID to a text file
        saveFile = open('sample.txt','a')

        saveFile.write(x+"\n")
        saveFile.close()
   
