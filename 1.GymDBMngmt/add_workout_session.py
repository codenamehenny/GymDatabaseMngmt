# This file adds a workout session to the Workout Sessions table to satisfy Task 2
from connect_mysql.py import connect_database
from mysql.connector import Error

conn = connect_database()
if conn:
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        try:
            cursor = conn.cursor()
            workout_info = (member_id, date, duration_minutes, calories_burned)

            # this will make sure the member is registered before adding the workout session
            cursor.execute("SELECT id FROM Members WHERE id = %s", (member_id,))
            member = cursor.fetchone()
            if not member:
                print(f"Cannot add workout session because member ID {member_id} is not registered.\nPlease register them first.")
                return

            #  this is the query to add a workout session to a registered member broken up in 2 lines for better readability
            query = """
            INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)        
            VALUES (%s, %s, %s, %s)
            """
            # executing the query and committing changes
            cursor.execute(query, workout_info)
            conn.commit()
            print(f"Workout session for member id {member_id} added successfully.")
        except Error as e:
            print(f"Error message: {e}. Workout session not recorded for {member_id}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
else:
    print("Connection to MYSQL failed")