"""
4 3
-1 -3 4 2

4 students, must have 3 on time (<=0).
"""

number_on_time = 3
students_arrivals = [-1, -3, 4, 2]

prompt_students = len([stu for stu in students_arrivals if stu <= 0])
if prompt_students >= number_on_time:
    print('YES')
else:
    print('NO')
