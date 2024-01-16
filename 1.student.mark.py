import os
STUDENT = []
COURSE = []
MARK = []


# Add new student info
def input_student():
    student_num = int(input("Enter number of student: "))
    print("------------------")
    for _ in range(student_num):
        stu = {}

        # Input student info
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        student_dob = input("Date of birth: ")
        print("------------------")
        
        # Insert info to the dictionary stu
        stu.update({"id": student_id})
        stu.update({"name": student_name})
        stu.update({"dob": student_dob})

        # Add info to the student list
        STUDENT.append(stu)



# Add new course info
def input_course():
    course_num = int(input("Enter number of courses: "))
    print("------------------")
    for _ in range(course_num):
        crs = {}

        # Input course info
        course_id = input("Course ID: ")
        course_name = input("Course name: ")
        print("------------------")

        # Insert info to the dictionary crs
        crs.update({"id": course_id})
        crs.update({"name": course_name})

        # Add info to the course list
        COURSE.append(crs)


# Input students' marks for a course
def input_marks():
    # Check if the student is in the list
    check_student = False
    print("--------------------------")
    student_id = input("Enter student's ID: ")
    if len(STUDENT) == 0:
        print("Can't find student!")
        return
    else:
        student_name = input("Enter student's name: ")
        for stu in STUDENT:
            id = stu.get("id")
            name = stu.get("name")
            if student_id == id and student_name == name:
                check_student = True
    if check_student == False:
        print("Can't find student!")
        return
    
    # Check if the course is in the list
    check_course = False
    course_id = input("Enter course's ID: ")
    if len(COURSE) == 0:
        print("Invalid course ID!")
        return
    else:
        for crs in COURSE:
            id = crs.get("id")
            if course_id == id:
                check_course = True
    if check_course == False:
        print("Invalid course ID!")
        return
    
    # Input student's marks
    student_mark = float(input("Enter mark: "))
    print("--------------------------")

    # Insert student's marks to the dictionary marks
    marks = {}
    marks.update({"student_id": student_id})
    marks.update({"student_name": student_name})
    marks.update({"course_id": course_id})
    marks.update({"student_mark": student_mark})

    # Add student's marks to the mark list
    MARK.append(marks)


# List out all the student
def list_student():
    print("\n-----------------------------------------------")
    print("List of all the student:")
    stt = 1
    for stu in STUDENT:
        student_name = stu.get("name")
        student_id = stu.get("id")
        student_dob = stu.get("dob")

        print(f"{stt}. ID: {student_id}, Name: {student_name}, Date of birth: {student_dob}")
        stt += 1
    print("-----------------------------------------------")



# List out all the course
def list_course(COURSE):
    print("\n-----------------------------------------------")
    print("List of all the course: ")
    stt = 1
    for crs in COURSE:
        course_id = crs.get("id")
        course_name = crs.get("name")

        print(f"{stt}. ID: {course_id}, Name: {course_name}")
        stt += 1
    print("-----------------------------------------------")



# List out marks of a course
def list_mark(MARK):
    search = input("Course ID: ")
    print("\n-----------------------------------------------")
    stt = 1
    for marks in MARK:
        student_id = marks.get("student_id")
        student_name = marks.get("student_name")
        course_id = marks.get("course_id")
        student_mark = marks.get("student_mark")

        if search == course_id:
            print(f"{stt}. ID: {student_id}, Name: {student_name}, Mark: {student_mark}")
            stt += 1
    print("-----------------------------------------------")


# Main function
def main():
    os.system('cls')

    while (True):
        print("\n==========Student Management System==========")
        print("1. Add new students")
        print("2. Add new courses")
        print("3. Enter the mark of a course for a student")
        print("4. List out all students")
        print("5. List out all courses")
        print("6. List out marks of all student of a course.")
        print("7. Exit.\n")

        choice = input("Your choice: ")
        match choice:
            case "1":
                input_student()
            case "2":
                input_course()
            case "3":
                input_marks()
            case "4":
                list_student()
            case "5":
                list_course(COURSE)
            case "6":
                list_mark(MARK)
            case "7":
                exit()
            case _:
                print("Invalid choice!")

# Call the main function
if __name__ == "__main__":
    main()