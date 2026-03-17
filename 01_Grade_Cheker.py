# 1. Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : "A"
# 80-89 : "B"
# 70-79 : "C"
# 60-69 : "D"
# Below 60 : "F"
# here we used a basic if else statement to carry out marks and all.

# Solution -->
marks = int(input('Enter your marks \n'))
if marks >=90:
  grade = 'A'
elif marks >=80 :
  grade = 'B'
elif marks >=70 :
  grade = 'C'
elif marks >=60 :
  grade = 'D'
else : grade = 'Fail'

print('your grade is: ' , grade)