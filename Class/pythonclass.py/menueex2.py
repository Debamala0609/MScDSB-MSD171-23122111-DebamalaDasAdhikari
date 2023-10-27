#
# Dictionary to store student details
student_records = {}

def add_student():
    roll_number = input("Enter student's roll number: ")
    name = input("Enter student's name: ")
    phone = input("Enter student's phone: ")
    email = input("Enter student's email: ")
    
    student_records[roll_number] = {
        "Name": name,
        "phone": phone,
        "email": email,
    }
    print(f"Student with roll number {roll_number} added successfully!")

def view_student():
    roll_number = input("Enter student's roll number to view details: ")
    student = student_records.get(roll_number)
    if student:
        print("Student Details:")
        print(f"Roll Number: {roll_number}")
        for key, value in student.items():
            print(f"{key}: {value}")
    else:
        print(f"Student with roll number {roll_number} not found!")

def update_student():
    roll_number = input("Enter student's roll number to update details: ")
    student = student_records.get(roll_number)
    if student:
        print("Current Student Details:")
        for key, value in student.items():
            print(f"{key}: {value}")
        
        name = input("Enter new name (press Enter to keep the current value): ")
        phone = input("Enter new phone (press Enter to keep the current value): ")
        email = input("Enter new email (press Enter to keep the current value): ")
        
        if name:
            student["Name"] = name
        if phone:
            student["phone"] = phone
        if email:
            student["email"] = email
        
        print("Student details updated successfully!")
    else:
        print(f"Student with roll number {roll_number} not found!")

def delete_student():
    roll_number = input("Enter student's roll number to delete: ")
    if roll_number in student_records:
        del student_records[roll_number]
        print(f"Student with roll number {roll_number} deleted successfully!")
    else:
        print(f"Student with roll number {roll_number} not found!")

def menu():
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()