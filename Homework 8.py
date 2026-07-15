# Student data: (Name, Marks)
students = [
    ("Alice", 85),
    ("Bob", 42),
    ("Charlie", 67),
    ("David", 35)
]

# Pass mark
pass_mark = 40

# Display results
print("Student Results")
print("----------------")

for student in students:
    name = student[0]
    marks = student[1]

    if marks >= pass_mark:
        result = "Pass"
    else:
        result = "Fail"

    print("Name:", name)
    print("Marks:", marks)
    print("Result:", result)
    print()