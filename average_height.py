student_heights = input().split()
print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(student_heights)

Height = 0
for i in student_heights:
  Height += i
print(Height)

average = Height / len(student_heights)

print(average)