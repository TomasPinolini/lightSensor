import retriever
# import dumper

from datetime import datetime

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

FOLDER = "data_light"

def main():
#     try:
#         retriever.openOrCreateDir(FOLDER)
#         today = datetime.today().strftime("%Y-%m-%d")
#         time = datetime.today().strftime("%H:%M:%S")
#         csv = f'{FOLDER}/{today}.csv'
        
#         ser = retriever.conn2Port(SERIAL_PORT, BAUD_RATE)
#         if not ser:
#             print("Serial port connection failed. Exiting program.")
#             return
        
#         retriever.writeCSV(csv, ser)
#         print(ser)

#         database = dumper.conn2DB(csv)
#         print(database)
#         if not database:

#             print("Database connection failed. Exiting program.")
#             return
        
#         dumper.insertData(database, csv, time)

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     finally:
#         if 'ser' in locals() and ser.is_open:
#             retriever.closeConn(ser)
#         if 'database' in locals():
#             dumper.closeDB(database)
    print("Initializing..")

if __name__ == "__main__":
    main()