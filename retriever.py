import serial
import csv
from datetime import datetime
import os

def openOrCreateDir(name):
    if not os.path.exists(name):
        os.makedirs(name)

def conn2Port(SP, BR):
    try:
        ser = serial.Serial(SP, BR)
        print("Serial port opened successfully!")
        return ser

    except serial.SerialException as e:
        print(f"Serial port error: {e}")



def writeCSV(csvfile, serial):
    with open(csvfile, mode='a', newline='') as file:
        writer = csv.writer(file)

        if os.stat(csvfile).st_size == 0:
            writer.writerow(['Timestamp', 'Sensor Value'])
            print(f"Writing data to {file}...")

        for i in range(0,3):
 
            data = serial.readline().decode().strip()  
            print(f"Received: {data}")

            timestamp = datetime.now().strftime('%H:%M:%S')
            writer.writerow([timestamp, data])


def closeConn(serial):
    if 'ser' in locals() and serial.is_open:
        serial.close()
        print("Serial port closed.")


