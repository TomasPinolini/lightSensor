import mysql.connector
from mysql.connector import Error
import csv
from datetime import datetime

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "123"  
DB_NAME = "sensorarduino"
TABLE_NAME = "light"

def conn2DB(csv):
    try:
        print("Connecting to the database...")
        conn = mysql.connector.connect(
            host = DB_HOST, 
            user = DB_USER, 
            password = DB_PASSWORD, 
            database = DB_NAME
        )
        if conn.is_connected(): print("Connection Successful")

    except Error as e:
        print(f"Database connection error: {e}")
        return None
    
    return conn 

    
def insertData(db,csv,time):
    try:
        cursor = db.cursor()
        print(f"Reading data from {csv}...")

        with open(csv, mode='r') as file:
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
        print(f"CSV file '{csv}' not found. Make sure the file exists.")  
    except Error as e:
        print(f"Database error: {e}")  
    finally:
        if 'db' in locals() and db.is_connected():
            db.close()
            print("Database connection closed.")

def closeDB(db):
    if db and db.is_connected():
        db.close()
        print("Database connection closed.")
