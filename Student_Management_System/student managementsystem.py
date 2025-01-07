import sys

class StudentManagement:
    def __init__(self):
        self.students = []
        self.current_id = 1

    def generate_unique_id(self):
        unique_id = self.current_id
        self.current_id += 1
        return unique_id

    def Add_student(self, name, email, phone, address, program, stream):
        student_id = self.generate_unique_id()
        enrollment_id = f"ENR{student_id:04d}"

        student = {
            "student_id": student_id,
            "enrollment_id": enrollment_id,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "program": program,
            "stream": stream,
            "course": []
        }
        self.students.append(student)
        print(f"Student added with ID: {student_id}")

    def Update_student(self, student_id, name=None, email=None, phone=None):
        for student in self.students:
            if student['student_id'] == student_id:
                if name:
                    student['name'] = name
                    print("Name updated")
                if email:
                    student['email'] = email
                    print("Email updated")
                if phone:
                    student['phone'] = phone
                    print("Phone updated")
                return
        print("Student ID not found")

    def Delete_student(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                self.students.remove(student)
                print(f"Student deleted: {student_id}")
                return
        print("Student ID not found")

    def Display_all_students(self):
        if not self.students:
            print("No students available")
            return
        print(f"{'ID':<10}{'NAME':<20}{'EMAIL':<30}{'PHONE':<15}{'ENROLLMENT':<15}{'PROGRAM':<10}{'STREAM':<10}{'COURSE':<20}")
        print("-" * 120)
        for student in self.students:
            courses = ', '.join(student['course']) if student['course'] else 'No courses assigned'
            print(f"{student['student_id']:<10}{student['name']:<20}{student['email']:<30}{student['phone']:<15}{student['enrollment_id']:<15}{student['program']:<10}{student['stream']:<10}{courses:<20}")

    def Display_student_by_id(self, student_id):
        for student in self.students:
            if student['student_id'] == student_id:
                print(f"ID: {student['student_id']} | Name: {student['name']} | Email: {student['email']} | Phone: {student['phone']} | Enrollment Number: {student['enrollment_id']} | Program: {student['program']} | Stream: {student['stream']}")
                return
        print("Student ID not found")

    def Assign_course(self, student_id, courses):
        for student in self.students:
            if student['student_id'] == student_id:
                student['course'].extend(courses)
                print(f"Course(s) {', '.join(courses)} assigned to student ID {student_id}")
                return
        print("Student ID not found")

    def User_menu(self):
        while True:
            result = input("1> Add student\n2> Update student\n3> Delete student\n4> Display all students\n5> Display student by ID\n6> Assign course to student\n7> Exit\nEnter your choice: ")
            if result == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                address = input("Enter address: ")
                program = input("Enter program: ")
                stream = input("Enter stream: ")
                self.Add_student(name, email, phone, address, program, stream)

            elif result == '2':
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter new name (leave blank to skip): ") or None
                email = input("Enter new email (leave blank to skip): ") or None
                phone = input("Enter new phone (leave blank to skip): ") or None
                self.Update_student(student_id, name, email, phone)

            elif result == '3':
                student_id = int(input("Enter student ID to delete: "))
                self.Delete_student(student_id)

            elif result == '4':
                self.Display_all_students()

            elif result == '5':
                student_id = int(input("Enter student ID to display: "))
                self.Display_student_by_id(student_id)

            elif result == '6':
                student_id = int(input("Enter student ID to assign courses: "))
                courses = input("Enter courses separated by commas: ").split(',')
                self.Assign_course(student_id, courses)

            elif result == '7':
                print("Exiting")
                sys.exit(0)

            else:
                print("Invalid input")

if __name__ == "__main__":
    obj = StudentManagement()
    obj.User_menu()
