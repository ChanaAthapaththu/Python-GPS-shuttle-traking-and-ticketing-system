import mysql.connector
# mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="rfiddata")

# mycursor=mydb.cursor()
# sqlform="Insert into devicedata( rfid,date,timein,latin,lngin)values(%s,%s,%s,%s,%s)"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="rfiddata"
)

mycursor = mydb.cursor()

sql = "INSERT INTO devicedata (rfid,date,timein,latin,lngin,timeout,latout,lngout,timetraveled,distancetraveled,travelfee) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
val = ("22", "1/7/2020", "", "", "", "", "", "", "", "","")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


   
  