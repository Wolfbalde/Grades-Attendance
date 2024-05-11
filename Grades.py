import pandas as pd

# Loading DataFrames
stud_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/StudentList.csv',
    usecols=["Email", "Name", "Roll No"],
)
stud_list = stud_list.sort_values(by="Roll No")

marks_list = pd.read_csv(
    'C:/Users/Akaash/Desktop/Grades/Grades-Attendance/Marks.csv',
    usecols=["Email", "Name", "Roll No", "Marks"],
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

print(final_data.to_string())