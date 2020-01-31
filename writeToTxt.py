x=input('Enter the RFID number')
saveFile = open('sample.txt','a')

saveFile.write(x+"\n")
saveFile.close()

 