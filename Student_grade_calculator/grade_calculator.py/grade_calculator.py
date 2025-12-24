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
