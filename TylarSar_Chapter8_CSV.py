# Create a program CSV that contains data on student's scores, and can be viewed after.

import csv

def enterGrades(filename):
    # Prompt user to enter number of students
    studentNum = int(input("Enter the number of students: "))

    # Organize list with titles
    data = [["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]]

    # Store data for the students separately
    for _ in range(studentNum):
        # Enter student's names
        firstName = input("Enter the student's first name: ")
        lastName = input("Enter the student's last name: ")

        # Enter student's exam scores
        exam1 = int(input("Enter student's Exam 1 score: "))
        exam2 = int(input("Enter student's Exam 2 score: "))
        exam3 = int(input("Enter student's Exam 3 score: "))
        data.append([firstName, lastName, exam1, exam2, exam3])

    # Add information to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"Data successfully written to {filename}")

def readData(filename):
    # Read data from CSV file and print in tabular format
    with open(filename, mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            print("{:<12} {:<12} {:<6} {:<6} {:<6}".format(*row))

# Run main
def main():
    filename = 'grades.csv'

    # Enter Data
    enterGrades(filename)

    # Read Data
    readData(filename)

if __name__ == "__main__":
    main()
