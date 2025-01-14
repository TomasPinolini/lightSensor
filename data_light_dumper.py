import mysql.connector
from mysql.connector import Error
import csv
from datetime import datetime

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""  
DB_NAME = "sensorarduino"
TABLE_NAME = "light"

today = datetime.now().strftime('%Y-%m-%d')
CSV_FILE = f'data_light/{today}.csv'

try:
    print("Connecting to the database...")
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = db.cursor()
    print(f"Connected to database '{DB_NAME}'.")
    print(f"Reading data from {CSV_FILE}...")

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        
        for row in reader:
            timestamp, value = row
            print(f"Inserting: {timestamp}, {value}")  
            sql = f"INSERT INTO {TABLE_NAME} (timestamp, value) VALUES (%s, %s)"
            cursor.execute(sql, (timestamp, value))

    db.commit()
    print("All data has been inserted into the database.")

except FileNotFoundError:
    print(f"CSV file '{CSV_FILE}' not found. Make sure the file exists.")  
except Error as e:
    print(f"Database error: {e}")  
finally:
    if 'db' in locals() and db.is_connected():
        db.close()
        print("Database connection closed.")
