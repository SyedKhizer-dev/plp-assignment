with open("students.txt", "r") as f:

    print(f.read().upper())


with open("students.txt", "r+") as f:
    students = [line.split(",") for line in f]
    print(students)
    total_students=len(students)

    scores = [int(student[1]) for student in students]
    print(scores)
    average = sum(scores) / len(scores)
    max_score=max(scores)

    print(f"Class Average: {average}")
    print(f"Max score: {max_score}")
    print(f"Total students: {total_students}")
    
    f.write(f"\nClass Average: {average} | Total Students: {total_students}")