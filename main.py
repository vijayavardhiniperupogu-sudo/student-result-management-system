from datetime import datetime

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


while True:
    print("\n===== Student Result Management System =====")

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    try:
        percentage = float(input("Enter Percentage: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    grade = calculate_grade(percentage)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n------ Result ------")
    print("Date:", current_time)
    print("Roll No:", roll_no)
    print("Name:", name)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("--------------------\n")

    # Save to file (professional format)
    with open("results.txt", "a") as file:
        file.write("===== Student Record =====\n")
        file.write(f"Date: {current_time}\n")
        file.write(f"Roll No: {roll_no}\n")
        file.write(f"Name: {name}\n")
        file.write(f"Percentage: {percentage}\n")
        file.write(f"Grade: {grade}\n")
        file.write("---------------------------\n\n")

    choice = input("Do you want to add another student? (yes/no): ")
    if choice.lower() != "yes":
        print("\nThank you for using the system 😊")
        break