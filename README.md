# Student_Grade_Calculator_Week_2-Task

🎓 Student Grade Calculator – Python Project

📌 Project Overview

The Student Grade Calculator is a Python-based console application developed to demonstrate core programming concepts such as decision-making, loops, functions, and input validation.

The program takes a student’s name and marks as input, validates the input, calculates the grade based on predefined grading rules, and displays an encouraging message accordingly.

This project is part of Week 2 – Making Decisions & Repeating Tasks in Python and focuses on applying real-life scenarios using Python fundamentals.


--

🎯 Project Objectives

To understand and apply if-elif-else conditions

To implement while loops for input validation

To create and use reusable functions

To handle invalid user inputs gracefully

To follow proper project structure and documentation practices



---

⚙️ Setup Instructions

Prerequisites

Python 3.x installed on your system

Any Python IDE (PyCharm, VS Code, IDLE)

GitHub account for submission


Steps to Run the Project

1. Clone or download the repository from GitHub


2. Navigate to the project folder


3. Run the program using the command:

python grade_calculator.py


4. Enter the student name and marks when prompted




---

🧠 Grading Logic

The grading system is implemented as follows:

Marks Range	Grade

90 – 100	A
80 – 89		B
70 – 79		C
60 – 69		D
0 – 59		F


Each grade is associated with an encouraging message displayed to the user.


---

🧩 Code Structure

student-grade-calculator/
│
├── grade_calculator.py     # Main Python program
├── README.md               # Project documentation
├── test_cases.txt          # Test cases and expected outputs
└── screenshots/            # Output screenshots


def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! 😊"
    elif marks >= 60:
        return "D", "You passed. Try to improve! 💪"
    else:
        return "F", "Don't worry, keep practicing! 🔁"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("🎓 Student Grade Calculator 🎓")
    student_name = input("Enter student name: ")

    marks = get_valid_marks()
    grade, message = get_grade(marks)

    print("\n📊 RESULT FOR", student_name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


if __name__ == "__main__":
    main()

---

🧑‍💻 Technical Details

Programming Concepts Used

Functions

get_grade(marks) – Determines grade and message

get_valid_marks() – Validates marks input using a while loop

main() – Manages program flow


Conditional Statements

if-elif-else used to assign grades


Loops

while loop used to repeatedly prompt user until valid input is given


Input Validation

Ensures marks are between 0 and 100

Handles non-numeric input using exception handling




---

🧪 Testing Evidence

All test scenarios were manually tested to ensure correctness.

Test Cases Included (test_cases.txt)

Valid inputs (A, B, C, D, F grades)

Boundary values (0, 100)

Invalid inputs (negative values, values > 100)

Non-numeric inputs (characters, symbols)


Expected outputs are documented and verified during execution.


---

🖼️ Visual Documentation

The screenshots/ folder contains:

Successful execution with valid input

Grade calculation output

Handling of invalid inputs

Error messages for incorrect entries


These screenshots serve as proof of correct functionality.


---

✅ Quality Standards Checklist

✔ Python code works correctly
✔ Uses functions
✔ Uses if-else conditions
✔ Uses while loop
✔ Input validation implemented
✔ README file included
✔ Test cases documented
✔ Screenshots provided
✔ GitHub repository structured properly

All required quality standards have been met for full marks.


---

📦 Submission Details

GitHub repository contains all required files

Clean and readable code structure

Proper documentation and testing evidence included



---

📝 Remarks

This project helped strengthen my understanding of Python fundamentals such as decision-making, looping, functions, and input validation. It improved my ability to write structured, readable, and user-friendly Python programs while following real-world project documentation standards.



