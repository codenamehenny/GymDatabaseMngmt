# This file adds members to the Members table in MYSQL 
from connect_mysql.py import connect_database

conn = connect_database()
if conn:
    add_member(id, name, age):
        try:
            # our "librarian" grabbing and inserting info to the "library"
            cursor = conn.curser() 

            # new member placed in tuple
            new_member = (id, name, age)

            # SQL query with spaceholders for reusability
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

            #Executing the query
            cursor.execute(query, new_member)
            conn.commit()
            print(f"'{name}' added to the Members table successfully")
        except Exception as e:
            print(f"Error Message: '{e}'. {name} has not been added successfully.")
        finally:
            # closing the cursor and connection to mysql
            if conn and conn.is_connected():
                cursor.close()
                conn.close()