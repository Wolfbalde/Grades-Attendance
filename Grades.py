import pandas as pd

# Loading DataFrames
stud_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/StudentList.csv',
    usecols=["Email", "Name", "Roll No"],
)
stud_list = stud_list.sort_values(by="Roll No")

marks_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/Marks.csv',
    usecols=["Email", "Name", "Roll No", "Marks1", "Marks2", "Marks3"],
)
marks_list = marks_list.sort_values(by="Roll No")

quiz_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/Quiz.csv',
    usecols=["Email", "Name", "Roll No", "Quiz 1", "Quiz 2", "Quiz 3"],
)
quiz_list = quiz_list.sort_values(by="Roll No")

attd_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/Attendance.csv',
    usecols=["Email", "Name", "Roll No", "Attendance"],
)
attd_list = attd_list.sort_values(by="Roll No")

# Merging DataFrames
final_data = pd.merge(stud_list, marks_list, on=["Email", "Name", "Roll No"], how="outer")
final_data = pd.merge(final_data,quiz_list, on=["Email", "Name", "Roll No"], how="outer")
final_data = pd.merge(final_data, attd_list, on=["Email", "Name", "Roll No"], how="outer")
final_data = final_data.fillna(0)

#mapping grades based on the marks scored
grades = {
    90: "A+",
    80: "A",
    70: "B",
    60: "C",
    50: "D",
    0: "F",
}

def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter


#display the mark percentage and attendance percentage
def student_attendance_grade_percentage(mark,attendance,quiz):
    attendance_percentage = (attendance/40)*100
    grade = (mark*0.5)+(quiz*0.5)
    print("The attendance percentage is: ",  round(attendance_percentage,2)
          ,"and the grade of this student is: ", grade_mapping(grade*100))


#Code starts here
bol=True
while bol:
    try:
        bol=False
        roll_no = int(input("Enter Roll No of the student you wish to find the grades for: "))
        if roll_no not in final_data['Roll No'].values:
            print("Invalid Roll No!")
            break
        row=final_data[final_data['Roll No'] == roll_no]
        mark1=row["Marks1"].iloc[0]
        mark2 = row["Marks2"].iloc[0]
        mark3 = row["Marks3"].iloc[0]
        mark = (mark1+mark2+mark3)/270
        quiz1 = row["Quiz 1"].iloc[0]
        quiz2 = row["Quiz 2"].iloc[0]
        quiz3 = row["Quiz 3"].iloc[0]
        quiz=(quiz1+quiz2+quiz3)/60
        attend=row["Attendance"].iloc[0]
        student_attendance_grade_percentage(mark,attend,quiz)
        cont=input("Do you wish to continue? (y/n): ")
        if cont=="y" or cont=="Y":
            bol=True
    except ValueError as e:
        print("Please enter some Roll No")
        break