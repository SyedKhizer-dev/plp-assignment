# (a)
def save_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError) as e:
        return e


print(save_divide(10, 2))
print(save_divide(10, 0))
print(save_divide("hello", 56))


# (b)
def read_student_file(filename):
    try:
        with open(filename, "r") as f:
            pass
    except FileNotFoundError as e:
        return e
    finally:
        print("File operation complete")


def main():
    print(read_student_file("students.txt"))
    print(read_student_file("students1.txt"))


if __name__ == "__main__":
    main()
