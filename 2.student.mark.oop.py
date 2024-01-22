import os
STUDENT = []
COURSE = []
MARK = []


class student:
    def __init__(self, id, name, dob):
        self._id = id
        self._name = name
        self._dob = dob

    def id(self):
        return self._id
    def name(self):
        return self._name
    def dob(self):
        return self._dob
    
    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}, D.O.B: {self._dob}"
        

class course:
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def id(self):
        return self._id
    def name(self):
        return self._name

    def __str__(self):
        return f"ID: {self._id}, Name: {self._name}"


class mark:
    def __init__(self, student_id, student_name, course_id, student_mark):
        self.__student_id = student_id
        self.__student_name = student_name
        self.__course_id = course_id
        self.__mark = student_mark

    def student_id(self):
        return self.__student_id
    def student_name(self):
        return self.__student_name
    def course_id(self):
        return self.__course_id
    def mark(self):
        return self.__mark
    
    def __str__(self):
        f"Student ID: {self.__student_id}, Student name: {self.__student_name}, Course: {self.__course_id}, Mark: {self.__mark}"  

# Add new student info
def input_student():
    student_num = int(input("Enter number of student: "))
    print("------------------")
    for _ in range(student_num):

        # Input student info
        student_id = input("Student ID: ")
        student_name = input("Student name: ")
        student_dob = input("Date of birth: ")
        print("------------------")
        
        # Add info of student to the student list
        stu = student(student_id, student_name, student_dob)
        STUDENT.append(stu)



# Add new course info
def input_course():
    course_num = int(input("Enter number of courses: "))
    print("------------------")
    for _ in range(course_num):

        # Input course info
        course_id = input("Course ID: ")
        course_name = input("Course name: ")
        print("------------------")

        # Add info to the course list
        new = course(course_id, course_name)
        COURSE.append(new)


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
        for student in STUDENT:
            if student_id == student.id() and student_name == student.name():
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
        for course in COURSE:
            if course_id == course.id():
                check_course = True
    if check_course == False:
        print("Invalid course ID!")
        return
    
    # Input student's marks
    student_mark = float(input("Enter mark: "))
    print("--------------------------")

    # Insert student's marks to the dictionary marks
    #marks = {}

    # Add student's marks to the mark list
    new = mark(student_id, student_name, course_id, student_mark)
    MARK.append(new)


# List out all the student
def list_student():
    print("\n-----------------------------------------------")
    print("List of all the student:")
    stt = 1
    for student in STUDENT:
        print(f"{stt}. ID: {student.id()}, Name: {student.name()}, Date of birth: {student.dob()}")
        stt += 1
    print("-----------------------------------------------")


# List out all the course
def list_course(COURSE):
    print("\n-----------------------------------------------")
    print("List of all the course: ")
    stt = 1
    for course in COURSE:
        print(f"{stt}. ID: {course.id()}, Name: {course.name()}")
        stt += 1
    print("-----------------------------------------------")



# List out marks of a course
def list_mark(MARK):
    search = input("Course ID: ")
    print("\n-----------------------------------------------")
    print("List of students' mark of the course:")
    stt = 1
    for mark in MARK:
        if search == mark.course_id():
            print(f"{stt}. ID: {mark.student_id()}, Name: {mark.student_name()}, Mark: {mark.mark()}")
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