import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        # Try to connect
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password', # Change this
            database='your_db_name'    # Change this
        )
        
        if conn.is_connected():
            print("✅ Connected successfully!")
            return conn

    except Error as e:
        # If it fails, tell us exactly why
        print(f"❌ Connection failed: {e}")
        return None

# Use the function
db = get_db_connection()

if db:
    # Do your database work here
    db.close()
    print("🔒 Connection closed.")
