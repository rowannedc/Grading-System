# Student Grading System (OOP in Python)

## Overview
This project is a simple Python program that demonstrates the application of 
Object-Oriented Programming (OOP) principles in a real-world scenario. 
It simulates a basic grading system where users can input student details, 
compute grade averages, and display remarks (Pass/Fail).

## Features
- Accepts multiple student records with validation for names and grades
- Computes the average of three grades for each student
- Provides remarks based on the computed average:
  - "Passed 🥳" if average ≥ 75
  - "Failed 😭" if average < 75
- Displays a class summary with student names, averages, and remarks

## OOP Principles Applied
- **Encapsulation**: Bundles student data (name, grades) and methods 
  (`compute_average`, `get_remark`) into the `Student` class.
- **Abstraction**: Hides system complexity and provides a simple 
  interface for adding students and displaying summaries.
- **Single Responsibility Principle (SRP)**: 
  - `Student` class handles individual student data and grade logic.
  - `GradingSystem` class manages the collection of students.

## How to Run
1. Clone the repository:<br>git clone https://github.com/your-username/student-grading-system.git

2. Navigate to the project folder:<br>
```cd student-grading-system```

3. Run the script:<br>
```python grading_system.py```

## Example

------- Student Details -------  
Enter number of students: 2  

🧑‍🎓 Student 1 Details 🧑‍🎓  
Enter student name: Alice  
Enter grade 1 (0-100): 90  
Enter grade 2 (0-100): 85  
Enter grade 3 (0-100): 92  

🧑‍🎓 Student 2 Details 🧑‍🎓  
Enter student name: Bob  
Enter grade 1 (0-100): 60  
Enter grade 2 (0-100): 70  
Enter grade 3 (0-100): 65  

------- Class Summary -------  
Alice - Average: 89.00, Remark: Passed 🥳  
Bob - Average: 65.00, Remark: Failed 😭  

## Author
Developed as part of an Object-Oriented Programming (OOP) exam exercise.
