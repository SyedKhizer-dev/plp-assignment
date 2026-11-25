import json
from student_tracker import load_students
from pathlib import Path


def main():
    try:
        filepath = (
            Path(__file__).resolve().parent
            / "student_tracker"
            / "data"
            / "students.json"
        )
        students = load_students(filepath)

        for student in students:
            print(f"Student: {student.name} | Average: {student.average}")

    except FileNotFoundError:
        print("JSON file doesn't exist")

    except json.JSONDecodeError:
        print("JSON file contains invalid JSON")

    except KeyError:
        print("A student record is missing name or scores")


if __name__ == "__main__":
    main()
