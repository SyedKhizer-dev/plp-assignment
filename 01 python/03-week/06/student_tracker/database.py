import json
from .models import Student


def load_students(filepath: str) -> list[Student]:
    with open(filepath) as f:
        data = json.load(f)
        students = [
            Student(name=record["name"], scores=record["scores"]) for record in data
        ]

    return students
