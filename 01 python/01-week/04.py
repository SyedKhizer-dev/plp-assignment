def calculate_grade(score, total=100, passing=50):
    try:
        if score < 0 or score > total:
            raise ValueError("Invalid input for score")

        percentage = score / total * 100

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= passing:
            grade = "D"
        else:
            grade = "F"

        return (percentage, grade)

    except ValueError as e:
        return e


print(calculate_grade(100))
print(calculate_grade(-7))
print(calculate_grade(500))
print(calculate_grade(75, 150, 60))


