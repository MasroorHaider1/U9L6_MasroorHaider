import mysql.connector


def establish_connection():
    connection = mysql.connector.connect(user='masroorh',
                                         password='223148222',
                                         host='10.8.37.226',
                                         database='masroorh_db')
    return connection


#these results are in a array list
def execute_command(connection, command):
    cursor = connection.cursor()
    cursor.execute(command)
    results = []

    for result in cursor:
        results.append(result)

    cursor.close()
    connection.close()

    return results

#this just runs the command
def get_student_info(connection, student_id):
    student_results = execute_command(connection, f"CALL GetStudentSchedule({student_id});")
    return student_results



#placed a parameter so when we do for result in the array of results coming from exectuing the execute command
def print_results(row):
    print(f"Period: {row[0]}")
    print(f"Course: {row[1]}")
    print(f"Room: {row[2]}")
    print(f"Teacher: {row[3]}\n")




def main():
    connection = establish_connection()

    results = get_student_info(connection, input("Enter student ID:"))

    for result in results:
        print()
        print_results(result)
    print()

    connection.close()


if __name__ == "__main__":
    main()
