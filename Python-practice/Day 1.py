'''Problem 1: Student Performance Analyzer
 Problem Statement:

You are given a list of students with their marks.
You need to:
Calculate average marks
Find topper
Find failed students (marks < 40)
Sort students by marks (descending)'''

students = {
    "Amit": 78,
    "Neha": 45,
    "Ravi": 32,
    "Priya": 90,
    "Karan": 39
}
def analyze_students(data):
    total_marks=0
    failed_students = []

# calculate total and find failed students
    for name,marks in data.items():
        total_marks+=marks
        if marks < 40:
            failed_students.append(name)
# avg_marks
    avg_marks=total_marks/len(data)

#topper
    topper=max(data, key=data.get)
    topper_marks=data[topper]

#sort students by marks
    sorted_students= sorted(data.items(), key=lambda x:x[1], reverse=True)

# Output
    print("----- Student Performance Report -----")
    print(f"Average Marks: {avg_marks:.2f}")
    print(f"Topper: {topper} ({topper_marks})")
    print(f"Failed Students: {failed_students}")
    print("Sorted Students (High to Low):")
    for name, marks in sorted_students:
        print(f"{name}: {marks}")

# Run function
analyze_students(students)
