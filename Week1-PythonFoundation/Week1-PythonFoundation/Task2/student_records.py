# student_records.py

students = []

def add_student(name, age, grade):
    students.append({"name": name, "age": age, "grade": grade})

def update_student(name, key, value):
    for student in students:
        if student["name"] == name:
            student[key] = value
            return True
    return False

def display_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print(student)

# Example usage
if __name__ == "__main__":
    add_student("Ali", 20, "A")
    add_student("Sara", 19, "B")
    update_student("Ali", "grade", "A+")
    display_students()
