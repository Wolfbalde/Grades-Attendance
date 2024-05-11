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

attd_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/Attendance.csv',
    usecols=["Email", "Name", "Roll No", "Attendance"],
)
attd_list = attd_list.sort_values(by="Roll No")

# Merging DataFrames
final_data = pd.merge(stud_list, marks_list, on=["Email", "Name", "Roll No"], how="outer")
final_data = pd.merge(final_data, attd_list, on=["Email", "Name", "Roll No"], how="outer")
final_data = final_data.fillna(0)

#mapping grades based on the marks scored
grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}

def grade_mapping(value):
    for key, letter in grades.items():
        if value >= key:
            return letter


#display the mark percentage and attendance percentage
def student_attendance_grade_percentage(mark,attendance):
    mark_percentage = mark*100
    attendance_percentage = (attendance/40)*100
    grade = grade_mapping(mark_percentage)
    print("The percentage of this student is: ", round(mark_percentage,2)," and the attendance percentage is: ",  round(attendance_percentage,2)
          ,"and the grade of this student is: ", grade)


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
        attend=row["Attendance"].iloc[0]
        student_attendance_grade_percentage(mark,attend)
        cont=input("Do you wish to continue? (y/n): ")
        if cont=="y" or cont=="Y":
            bol=True
    except ValueError as e:
        print("Please enter some Roll No")
        break