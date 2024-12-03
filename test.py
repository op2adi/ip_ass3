# class Course:
#     def __init__ (self, name, credits, assessments, policy):
#         self.name = name
#         self.credits = credits
#         self.assessments = assessments
#         self.policy = policy
#         self.students = {}

#     def add_student(self, student):
#         self.students[student.rollno] = student

#     def grade_students(self):
#         for student in self.students.values():
#             student.calculate_total_marks()
#             student.determine_grade(self.policy)

#     def summary(self):
#         grades = {grade: 0 for grade in ['A', 'B', 'C', 'D', 'F']}
#         for student in self.students.values():
#             grades[student.grade] += 1
#         print("Summary for course:", self.name)
#         print("Credits:", self.credits)
#         print("Assessments:", self.assessments)
#         print("Grading policy:", self.policy)
#         print("Grades distribution:", grades)

#     def save_grades(self, filename):
#         with open(filename, 'w') as f:
#             for student in self.students.values():
#                 f.write(f"{student.rollno},{student.total_marks},{student.grade}\n")

#     def search_student(self, rollno):
#         if rollno in self.students:
#             student = self.students[rollno]
#             print("Student details:")
#             print("Rollno:", student.rollno)
#             print("Marks in assessments:", student.marks)
#             print("Total marks:", student.total_marks)
#             print("Grade:", student.grade)
#         else:
#             print("Student not found.")


# class Student:
#     def _init_(self, rollno, marks):
#         self.rollno = rollno
#         self.marks = marks
#         self.total_marks = 0
#         self.grade = ''

#     def calculate_total_marks(self):
#         self.total_marks = sum(self.marks.values())

#     def determine_grade(self, policy):
#         for i in range(len(policy) - 1, -1, -1):
#             if self.total_marks >= policy[i]:
#                 self.grade = chr(ord('A') + i)
#                 return


# def upload_marks(course, filename):
#     with open(filename, 'r') as f:
#         for line in f:
#             parts = line.strip().split(',')
#             rollno = parts[0]
#             marks = {course.assessments[i][0]: float(parts[i + 1]) for i in range(len(course.assessments))}
#             student = Student(rollno, marks)
#             course.add_student(student)


# def do_grading(course):
#     course.grade_students()
#     course.summary()
#     course.save_grades("grades.txt")

# cname, credits = "IP", 4
# assessments = [("labs", 30), ("midsem", 15),("assignments", 10),("endsem", 35)]
# policy = [80, 70, 60, 50, 40, 0]
# course = Course(cname, credits, assessments, policy)
# upload_marks(course, "marks.txt")
# do_grading(course)
# a='1220'
# a=a.split()
# a.reverse()
# print(a)
# # l=[1,2,3,4,4,5,4]
# # i=4
# # for j in l:
# #     if j==i:
#         print(l.index(j))
# s='sanyam is sanyam'
# print(s.count('sanyam'))
a=(1,2,3)
print(a.reverse())