__author__ = 'GoldenGate'
import random
chart = {}
students= ["Peter", "Julian", "Johanna", "Robert", "Isabelle"]
seated = []
#assigning seat numbers to keys
for seats in range(len(students)):
    chart.update({seats: None})
#assigning students to values
for i in chart:
    chosen_one = random.choice(students)
    seated.append(chosen_one)
    students.remove(chosen_one)
    chart[i] =chosen_one
print students
print seated
print chart