import serial
import csv
from datetime import datetime
import os

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

if not os.path.exists('data_light'):
    os.makedirs('data_light')

current = datetime.now().strftime('%Y-%m-%d')
CSV_FILE = f'data_light/{current}.csv'

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    print("Serial port opened successfully!")

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        if os.stat(CSV_FILE).st_size == 0:
            writer.writerow(['Timestamp', 'Sensor Value'])
            print(f"Writing data to {CSV_FILE}...")

        for i in range(0,10):
        # while True:  
            try:
                data = ser.readline().decode().strip()  
                print(f"Received: {data}")

                timestamp = datetime.now().strftime('%H:%M:%S')
                writer.writerow([timestamp, data])

            except Exception as e:
                print(f"Error reading or writing data: {e}")

except serial.SerialException as e:
    print(f"Serial port error: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")
