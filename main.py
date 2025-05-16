
import mysql.connector

def establish_connection():
    return mysql.connector.connect(
        user='masroorh',
        password='223148222',
        host='10.8.37.226',
        database='masroorh_db'
    )

def execute_command(connection, command):
    cursor = connection.cursor()
    cursor.execute(command)
    results = []
    for result in cursor:
        results.append(result)
    cursor.close()
    connection.close()
    return results

def print_schedule(row):
    print("Period: " + str(row[0]))
    print("Course: " + str(row[1]))
    print("Room: " + str(row[2]))
    print("Teacher: " + str(row[3]))
    print()  # Newline

def main():
    # Ask if user is a Teacher (1) or Student (2)
    print("Are you a Teacher or Student?")
    print("1 for Teacher")
    print("2 for Student")
    choice = input("Enter choice (1 or 2): ")

    # Set boolean (True if Teacher, False otherwise)
    isTeacher = (choice == '1')

    # Get ID (basic if-else, no .strip())
    if isTeacher:
        id_input = input("Enter your Teacher ID: ")
    else:
        id_input = input("Enter your Student ID: ")

    # Fetch schedule
    connection = establish_connection()

    if isTeacher:
        results = execute_command(connection, "CALL GetTeacherSchedule(" + id_input + ");")
        print("\nTeacher Schedule for ID " + id_input + ":")
    else:
        results = execute_command(connection, "CALL GetStudentSchedule(" + id_input + ");")
        print("\nStudent Schedule for ID " + id_input + ":")

    # Print schedule
    for result in results:
        print_schedule(result)

if __name__ == "__main__":
    main()
