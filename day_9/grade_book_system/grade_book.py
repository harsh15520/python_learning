class Student:
    @staticmethod
    def student_record(data: dict[str, dict]):
        """Display all student records"""
        if not data:
            print('--Student record is empty--')
        else:
            print('--Student Records--')
            for student, subject_grades in data.items():
                print(f'{student}: {subject_grades}')
    
    @staticmethod
    def add_record(data: dict[str, dict]):
        """Add or update student records"""
        student = input('Enter student name: ').strip()
        
        if not student:
            print('Student name cannot be empty!')
            return
        
        subject_list = {}
        
        while True:
            subject = input('Enter subject (or "done" to stop): ').strip()
            if subject.lower() == 'done':
                break
            
            if not subject:
                print('Subject name cannot be empty!')
                continue
                
            grade = input(f'Enter grade for {subject}: ').strip().upper()
            subject_list[subject] = grade
        
        if not subject_list:
            print('No subjects were added!')
            return
        
        # Initialize student record if doesn't exist
        if student not in data:
            data[student] = {}
        
        # Update with new subjects only (preserve existing)
        data[student].update({subject: grade for subject, grade in subject_list.items()})
        
        print(f'{student} added/updated successfully')
    @staticmethod
    def bulk_student_registration(data):
        student_count=0
        Default_grade='D'
        while(True):
            student=input("enter name of student or done to stop").strip()
            if student.lower()=='done':
                break
            if not (student):
                print("--student name cannot be empty--")
                continue
            if student in data:
                print(f"{student} already present")
                continue
            else:
                student_count+=1
                subject=input("enter name of subjects seperated by commma").strip()
                if not subject:
                    print("--subject name cannot be empty--")
                    continue
                else:
                    subjects = [s.strip() for s in subject.split(',')]
                    data[student]=dict.fromkeys(subjects,Default_grade)
                    print(f'for {student} ,{subjects} these subjects are added')
        print(f"total number of registrations are:{student_count}")
    @staticmethod
    def remove(data):
        response=input("want to remove student/subject:\n").strip()
        if response.lower()=='student':
            student=input("enter name of student:\n").strip()
            data.pop(student,None)
        elif response.lower()=='subject':
            subjects=input('enter subjects seperated by commas').strip()
            subject=[s.strip() for s in subjects.split(',')]
            subject_response=input('remove from all students(Y)/from specific student(N),reply:Y/N :\n')
            if(subject_response.upper()=='Y'):
                for student in data:
                    for single_subject in subject:
                        data[student].pop(single_subject,None)
            elif(subject_response.upper()=='N'):
                student_name=input('enter student name:\n')
                for single_subject in subject:
                    data[student_name].pop(single_subject,None)
            else:
                return "--invalid selection--"
        else:
            return "--invalid selection--"

    @staticmethod
    def average_grade(data: dict[str, dict]):
        """Calculate average grade for a student"""
        student = input('Enter student name: ').strip()
        
        if student not in data:
            print('Student not found')
            return
        
        student_subjects = data[student]  # This is already a dictionary!
        if not student_subjects:
            print('No subjects found for student')
            return
        
        total_marks = 0
        subject_count = 0
        
        # Grade to marks mapping - cleaner than if-elif chains
        grade_points = {
            'A+': 100, 'A': 90, 'B+': 85, 'B': 80, 
            'C+': 75, 'C': 70, 'D+': 65, 'D': 60, 
            'E': 50, 'F': 0
        }
        
        for subject, grade in student_subjects.items():  # Proper dictionary iteration
            if grade in grade_points:
                total_marks += grade_points[grade]
                subject_count += 1
            else:
                print(f'Invalid grade "{grade}" found for {subject}')
                return
        
        average = total_marks / subject_count
        print(f'{student} average grade is {average:.2f}')

# Main program
records = {}

while True:
    print('\n--- Student Management System ---')
    print('1) View records')
    print('2) Add record')
    print('3) Calculate average grade')
    print('4) Bulk student registration')
    print('5) remove student/subject')
    print('6) exit')
    
    try:
        choose_number = int(input('Enter your choice: '))
        
        if choose_number == 1:
            Student.student_record(records)
        elif choose_number == 2:
            Student.add_record(records)  # Only pass records
        elif choose_number == 3:
            Student.average_grade(records)  # Only pass records
        elif choose_number == 4:
            Student.bulk_student_registration(records)
        elif choose_number == 5:
            Student.remove(records)
        elif choose_number == 6:
            print("exit")
            break
        else:
            print('Invalid choice')
            
    except ValueError:
        print('Invalid input. Please enter a number.')
    except KeyboardInterrupt:
        print('\nExiting...')
        break
