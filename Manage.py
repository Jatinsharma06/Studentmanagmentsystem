# Student Management System

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print("-" * 30)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists!")
        else:
            student = Student(student_id, name, age, grade)
            self.students[student_id] = student
            print(f"Student {name} added successfully.")

    def view_student(self, student_id):
        if student_id in self.students:
            self.students[student_id].display_info()
        else:
            print("Student not found.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id in self.students:
            student = self.students[student_id]
            if name:
                student.name = name
            if age:
                student.age = age
            if grade:
                student.grade = grade
            print(f"Student {student_id} updated successfully.")
        else:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student {student_id} deleted successfully.")
        else:
            print("Student not found.")

    def view_all_students(self):
        if self.students:
            for student in self.students.values():
                student.display_info()
        else:
            print("No students to display.")

def main():
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            grade = input("Enter Student Grade: ")
            sms.add_student(student_id, name, age, grade)

        elif choice == "2":
            student_id = input("Enter Student ID: ")
            sms.view_student(student_id)

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            grade = input("Enter new grade (leave blank to skip): ")
            age = int(age) if age else None
            sms.update_student(student_id, name or None, age, grade or None)

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            sms.delete_student(student_id)

        elif choice == "5":
            sms.view_all_students()

        elif choice == "6":
            print("Exiting the Student Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
