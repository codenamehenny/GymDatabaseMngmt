#2. Advanced Data Analysis in Gym Management System
#Task 1: SQL BETWEEN Usage
#Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.

from connect_mysql.py import connect_database
from mysql.connector import Error

conn = connect_database()
if conn:
    def get_members_in_range(start_age, end_age):
        try:
            age_range = (start_age, end_age)
            cursor = conn.cursor()

            # query using between to grab members within 25 and 30
            query = """
            SELECT id, name, age FROM Members
            WHERE age BETWEEN %s AND %s
            """
            cursor.execute(query, age_range)
            result = cursor.fetchall()
            # Organizing the results by index
            if result:
                print(f"Results for members between the ages {start_age} and {end_age}:")
                for row in result:
                    print(f"ID:{row[0]} -- Name: {row[1]} -- Age: {row[2]}")
            else:
                print(f"No member found within that age range. Adjust the range and try again.")
        except Error as e:
            print(f"Error Message: '{e}'. Cannot execute age range search")
        finally:
            # closing the cursor and connection to mysql
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
else:
    print("Connection to MYSQL failed")