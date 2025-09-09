import math
score1 = float(input('Enter score on Exam 1 (out of 50):\n'))
score2 = float(input('Enter score on Exam 2 (out of 50):\n'))
score3 = float(input('Enter score on Exam 3 (out of 50):\n'))
score4 = float(input('Enter score on Exam 4 (out of 50):\n'))

overall_grade = ((score1 / 50) + (score2 / 50) + (score3 / 50) + (score4 / 50)) / 4

print('Your overall grade is:', overall_grade * 100)

score5 = float(input('Enter score on Exam 5 (out of 50):\n'))
score6 = float(input('Enter score on Exam 6 (out of 50):\n'))
score7 = float(input('Enter score on Exam 7 (out of 75):\n'))
score8 = float(input('Enter score on Exam 8 (out of 75):\n'))

overall_grade2 = ((score5 / 50) + (score6 / 50) + (score7 / 75) + (score8 / 75)) / 4

print('Your overall grade is:', overall_grade2 * 100)

score9 = float(input('Enter score on Exam 9 (out of 100):\n'))
score10 = float(input('Enter score on Exam 10 (out of 100):\n'))
score11 = float(input('Enter score on Exam 11 (out of 100):\n'))
score12 = float(input('Enter score on Assignment 12 (out of 50):\n'))
score13 = float(input('Enter score on Assignment 13 (out of 50):\n'))
score14 = float(input('Enter score on Assignment 14 (out of 50):\n'))
score15 = float(input('Enter score on Assignment 15 (out of 50):\n'))

avg_exam = (score9 + score10 + score11) / 3
avg_assignment = (((score12 / 50) + (score13 / 50)  + (score14 / 50) + (score15 / 50)) / 4) *100
print('average exam', avg_exam)
print('average assignment', avg_assignment)
overall_grade3 = (avg_exam * 0.6) + (avg_assignment * 0.4)
print(overall_grade3)

