'''Concept used:
conditional statements - To implement a logic
loops - to run menu system
dictionry - To store data

What it does?
Teacher can do following tasks:
1- Add Student
2- View all Students
3- Check result
4- exit
'''
student = {}  #empty dictionary
print("\n~-----STUDENT MANAGER APP-----~")
while True:

    print("1. Add students")
    print("2. View students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    #Add Students
    if choice == "1":
        name = input("Enter Student Name:\n")
        marks = int(input("Enter Marks: "))
        student[name] = marks
        print(f"{name} Successfully Added!")

    #View Students
    elif choice == "2":
        if not student:
            print("No Student Found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)
                print()
    #Check Result
    elif choice == "3":
        name = input("Enter student name: ")
        if name in student:
            marks = student[name]

            if marks >= 30:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found!")

    #Exit
    elif choice == "4":
        print("Exiting....")
        break
    else:
        print("Invalid input!")