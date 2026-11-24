import json
from student_tracker import load_students


def main():
    try:
        students = load_students("student_tracker/data/students.json")

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
