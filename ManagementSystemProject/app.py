import json
from abc import ABC, abstractmethod
from pathlib import Path

database = "S:\Python\ManagementSystemProject\school_data.json"
data = {"students": [], "teachers": []}

if Path(database).exists():
    with open(database, "r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)


class Persons(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email


class Students(Persons):
    def get_roles(self):
        return "student"

    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        mob_no = int(input("Enter your mobile number: "))
        email = input("Enter your email address: ")

        if not Persons.validate_email(email):
            print("Invalid email")
            return

        roll_no = len(data["students"]) + 1

        data["students"].append(
            {
                "roll_no": roll_no,
                "name": name,
                "age": age,
                "mob_no": mob_no,
                "email": email,
                "grades": {},
            }
        )

        save()
        print(
            f"{name} got registered as student and assigned {roll_no} as his roll number."
        )

    def show_details(self):
        roll = int(input("Enter roll number: "))

        for student in data["students"]:
            if student["roll_no"] == roll:
                print("Details of student are as follows: ")
                print(f"Name : {student['name']}")
                print(f"Age : {student['age']}")
                print(f"Mobile number : {student['mob_no']}")
                print(f"Email : {student['email']}")
                print(f"Grades: {student['grades']}")
            else:
                print(f"Student of roll number {roll} not found.")

    def add_grades(self):
        roll_no = int(input("Enter your roll number: "))
        subject = input("Enter subject: ")
        marks = int(input("Enter marks: "))

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                i["grades"][subject] = marks
                save()
                print("Grades added successfully.")
            else:
                print(f"Student of roll number {roll_no} not found.")


class Teachers(Persons):
    def get_roles(self):
        return "teacher"

    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        mob_no = int(input("Enter you mobile number: "))
        email = input("Enter your email: ")

        if not Persons.validate_email(email):
            print("Invalid Email")

        reg_no = len(data["teachers"]) + 1

        data["teachers"].append(
            {
                "reg_no": reg_no,
                "name": name,
                "age": age,
                "mob_no": mob_no,
                "email": email,
            }
        )
        save()
        print(
            f"{name} got registered as teacher and assigneed {reg_no} as register number."
        )

    def show_details(self):
        reg_no = int(input("Enter register number: "))
        for teacher in data["teachers"]:
            if teacher["reg_no"] == reg_no:
                print("Details of teacher are as follows: ")
                print(f"Name: {teacher['name']}")
                print(f"Age: {teacher['age']}")
                print(f"Mobile number: {teacher['mob_no']}")
                print(f"Email: {teacher['email']}")
            else:
                print(f"Teacher of register number {reg_no} not found.")


stud = Students()
teach = Teachers()

print("Enter 1 to register as student ")
print("Enter 2 to register as teacher ")
print("Enter 3 to add grades ")
print("Enter 4 to see details of student ")
print("Enter 5 to see details of teacher ")


choice = int(input("Enter your choice: "))

if choice == 1:
    stud.register()

if choice == 2:
    teach.register()

if choice == 3:
    stud.add_grades()

if choice == 4:
    stud.show_details()

if choice == 5:
    teach.show_details()
