class Student:  # Accept and store student details (name, grades)
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def compute_average(self): 
        return sum(self.grades) / len(self.grades)  # Calculate the average of the grades, len for counting the number of grade input (3 grades in this case)
    
    def get_remark(self):
        return "Passed 🥳" if self.compute_average() >= 75 else "Failed 😭"
    
class GradingSystem:
    def __init__(self):
        self.students = []  # Store student objects and their computed averages and remarks

    def add_student(self, num_of_stud):
        for student_num in range(num_of_stud):  # Loop to add multiple students based on user input on number of students
            print(f"\n🧑‍🎓 Student {student_num + 1} Details 🧑‍🎓") 
            
            # Loop to enter student name with validation
            while True:
                name = input("Enter student name: ").strip()    
                if not name:
                    print("Name cannot be empty. Please enter a valid name.")
                elif any(char.isdigit() for char in name):  # Check if name contains any digits 
                    print("Name cannot be or cannot contain a number. Please enter a valid name.")
                else:
                    break  # Exit the loop if the name is valid

            grades = []
            for i in range(3):  # Loop to enter 3 grades for each student
                while True:  # Loop to enter grades with validation
                    try:
                        grade = float(input(f"Enter grade {i+1} (0-100): "))
                        if 0 <= grade <= 100:
                            grades.append(grade)  # Append valid grades to the grades list
                            break
                        else:
                            print("Grade must be between 0 and 💯. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric grade.")
                
            student = Student(name, grades)  # Create a Student object with name and grades
            self.students.append(student)   # Append the student object to the students list in GradingSystem
       
    def display_summary(self):
        print("\n", "-"*7, "Class Summary", "-"*7)
        for student in self.students:
            print(f"{student.name.capitalize()} - Average: {student.compute_average():.2f}, Remark: {student.get_remark()}")  # Display student name, average, and remark

grading_system = GradingSystem()  # Create an instance of GradingSystem

print("\n", "-"*7, "Student Details", "-"*7)
while True:  # Enter number of students with validation
    try:
        num_of_stud = int(input("Enter number of students: "))
        if num_of_stud > 0:
            break
        else:
            print("Number of students must be greater than zero. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

grading_system.add_student(num_of_stud)  # Add students to the grading system
grading_system.display_summary()  # Display the class summary


# OOP Pillars used: Encapsulation and Abstraction
# Encapsulation - bundle the data (student name, age, grades) and methods (compute_average, get_remark) into a single class (Student).
# Abstraction - hide the complexity of the grading system and provide a simple interface for adding students and displaying their summary.

# SOLID Principles used: Single Responsibility Principle (SRP)
# Single Responsibility Principle (SRP) - each class has a single responsibility: Student class handles student data and grading, GradingSystem class manages the collection of students.

