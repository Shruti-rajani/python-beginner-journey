Student_manager = {}

def add_student():
    name = input("Enter Student name here: ")
    marks = int(input("Enter student marks here: "))
    Student_manager[name] = marks
    print("Name and Marks has been added sucesfully!")

def get_marks():
    name = input("Enter the name of student here: ")
    if name in Student_manager:
        print(Student_manager[name])

def avg_marks():
    if not Student_manager:
        print("No students added yet.")
    else:
        total = sum(Student_manager.values())
        count = len(Student_manager)
        average = total / count
        print("Average Marks:", average)
        
while True:
    print("Menu:")
    print("1. Add student")
    print(("2. Get Marks"))
    print("3. Show Avarage")
    print('4. Exist')
    try:
        choice = int(input("Enter you choice here: "))
    except ValueError:
        print("Enter a valid choice")
        continue 

    if choice == 1:
        add_student()
    elif choice == 2:
        get_marks()
    elif choice == 3:
        avg_marks()
    else:
        print("Exist")
        break
