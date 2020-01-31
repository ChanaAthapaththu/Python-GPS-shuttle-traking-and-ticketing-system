x=input('Enter the RFID number')

with open('sample.txt') as f:
    if x in f.read():
        print("Out")

    else: print("IN")
    f.close()