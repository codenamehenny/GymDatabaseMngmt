# this file deletes workout sessions to satisfy task 4
from connect_mysql.py import connect_database
from mysql.connector import Error

conn = connect_database()
if conn:
    def delete_workout_session(session_id):
        try:
            cursor = conn.cursor()
            # checking if the session exists first
            cursor.execute("SELECT session_id FROM WorkoutSessions WHERE session_id = %s")
            session = cursor.fetchone()
            if not session:
                print(f"Workout session ID {session_id} was never registered. No further action required.")
                return
            # query to delete workout session
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            conn.commit()
            print(f"Workout session ID {session_id} has been deleted successfully")
        except Error as e:
            print(f"Error Message: {e}. Workout session ID {session_id} could not be deleted.")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
else:
    print("Connection to MYSQL failed")