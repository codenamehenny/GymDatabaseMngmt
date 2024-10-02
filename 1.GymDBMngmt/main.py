#1. Gym Database Management with Python and SQL
# Establishing Connection to Gym Database in MYSQL

import mysql.connector
from mysql.connector import Error


def connect_database():
    # Database conenction parameters
    db_name = "gym_db"
    user = "root"
    password = " "
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print(f"Connected to MYSQL '{db_name}' successfully")
    except Error as e:
        print(f"Error Message: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            print("MYSQL connection is now closed.")9=-[op];m,,mkl