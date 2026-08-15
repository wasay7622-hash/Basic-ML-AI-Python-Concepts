# Basic ML/AI Python Concepts Project

# 1. Variables and Data Types
student_name = "Ali"
age = 21
study_hours = 4.5
is_student = True

print("Student Name:", student_name)
print("Age:", age)
print("Study Hours:", study_hours)
print("Is Student:", is_student)

# 2. Conditional Statements
if study_hours >= 4:
    performance = "Good"
elif study_hours >= 2:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("Performance:", performance)

# 3. Loops
marks = [75, 82, 68, 90, 78]

print("\nMarks:")
for mark in marks:
    print(mark)

total = 0
i = 0
while i < len(marks):
    total += marks[i]
    i += 1

average = total / len(marks)
print("Average Marks:", average)

# 4. Functions
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def check_result(average_marks):
    if average_marks >= 50:
        return "Pass"
    return "Fail"

avg = calculate_average(marks)
result = check_result(avg)

print("Calculated Average:", avg)
print("Result:", result)

# 5. List Comprehension
passed_marks = [mark for mark in marks if mark >= 50]
print("Passed Marks:", passed_marks)

# 6. Dictionary Comprehension
subjects = {
    "Python": 85,
    "AI": 78,
    "Math": 72,
    "English": 80
}

high_marks = {subject: mark for subject, mark in subjects.items() if mark >= 80}
print("Subjects with 80 or more marks:", high_marks)

# 7. Exception Handling
try:
    number = int(input("\nEnter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a number.")

# 8. File Handling
file_name = "student_data.txt"

try:
    with open(file_name, "w") as file:
        file.write("Student Name: " + student_name + "\n")
        file.write("Average Marks: " + str(avg) + "\n")
        file.write("Result: " + result + "\n")

    with open(file_name, "r") as file:
        data = file.read()

    print("\nData saved in file:")
    print(data)

except OSError as error:
    print("File error:", error)

# 9. Classes and Objects
class Student:
    def __init__(self, name, age, average_marks):
        self.name = name
        self.age = age
        self.average_marks = average_marks

    def display_info(self):
        print("\nStudent Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Average Marks:", self.average_marks)

student1 = Student("Ali", 21, avg)
student1.display_info()

# 10. Modules and Packages
import math

number = 25
print("\nSquare root of", number, "is", math.sqrt(number))

print("\nProject completed successfully!")
