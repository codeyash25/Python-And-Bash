# 2 Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.

# Used dictionary and basic operations. Using if else:

# solution -->
catlogue={
  "Yash": 'A',
  "harsh": 'A+',
  "Mansi": 'A+',
  'Rohit': 'B',
  'Rahul': 'C'
}

print("Initial catalogue:",catlogue)

name = input("Enter the name of the student \n")
grade = input("Enter the grade of the student \n")

if name in catlogue:
  catlogue[name] = grade
  print("Updated catalogue:",catlogue)
else:
  catlogue[name] = grade
  print("Catalogue with new entry:",catlogue)

print(catlogue)