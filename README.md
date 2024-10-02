This is the Gym Database Management System.
The connection to the gym_db database in MYSQL is made in the connect_mysql.py file
~ Here's the layout the database without adding data ~
create database gym_db;
USE gym_db;
CREATE TABLE Members (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE WorkoutSessions (
	id INT AUTO_INCREMENT PRIMARY KEY,
	date DATE NOT NULL,
    duration_minutes INT NOT NULL,
    calories_burned INT NOT NULL,
    member_id INT,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
    
~ Here are all the tasks and where to find them ~
1. Gym Database Management with Python and SQL
Task 1: Add a Member

Write a Python function to add a new member to the 'Members' table in the gym's database.
    # Example code structure
    def add_member(id, name, age):
        # SQL query to add a new member
        # Error handling for duplicate IDs or other constraints
Expected Outcome: A Python function that successfully adds a new member to the 'Members' table in the gym's database. The function should handle errors gracefully, such as duplicate member IDs or violations of other constraints.
This task is found in the add_member.py file

Task 2: Add a Workout Session

Develop a Python function to add a new workout session to the 'WorkoutSessions' table for a specific member.
    # Example code structure
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        # SQL query to add a new workout session
        # Error handling for invalid member ID or other constraints
Expected Outcome: A Python function that adds a new workout session to the 'WorkoutSessions' table in the gym's database for a specific member. The function should handle errors gracefully, such as invalid member IDs or violations of other constraints.
This task is found in the add_workout_session.py file

Task 3: Updating Member Information

Implement a function to update the age of a member. Ensure that your function checks if the member exists before attempting the update.
    # Example code structure
    def update_member_age(member_id, new_age):
        # SQL query to update age
        # Check if member exists
        # Error handling
Expected Outcome: A Python function that updates the age of a member and handles cases where the member does not exist.
This task is found in the update_member.py file

Task 4: Delete a Workout Session

Create a Python function to delete a workout session based on its session ID. Include error handling for cases where the session ID does not exist.
    # Example code structure
    def delete_workout_session(session_id):
        # SQL query to delete a session
        # Error handling for non-existent session ID
Expected Outcome: A Python function that can delete a workout session using its session ID, with proper error handling for invalid IDs.
This task is found in the delete_workout.py file

2. Advanced Data Analysis in Gym Management System
Task 1: SQL BETWEEN Usage

Problem Statement: Retrieve the details of members whose ages fall between 25 and 30.
Expected Outcome: A list of members (including their names, ages, etc) who are between the ages of 25 and 30.
Example Code Structure:
    def get_members_in_age_range(start_age, end_age):
        # SQL query using BETWEEN
        # Execute and fetch results