# this file updates the member's age to satisfy task 3
from connect_mysql.py import connect_database
from mysql.connector import Error

conn = connect_database()
if conn:
    def update_member_age(member_id, new_age):
        try:
            cursor = conn.cursor()
            updated_member(new_age, member_id) # placed age first to align with query spaceholders
            # this will make sure the member is registered before updating the member
            cursor.execute("SELECT id FROM Members WHERE id = %s", (member_id,))
            member = cursor.fetchone()
            if not member:
                print(f"Cannot update member because member ID {member_id} is not registered.\nPlease register them first.")
                return
            # query to update member, executing it and committing it
            query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(query, updated_customer)
            conn.commit()
            print(f"Age for member ID {member_id} has been successfully updated to {new_age}")
        except Error as e:
            print(f"Error Message: {e}. Age for member ID {member_id} was not successfully updated.")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
else:
    print("Connection to MYSQL failed")