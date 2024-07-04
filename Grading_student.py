student_score = {
    "harry" : 81,
    "Ron" : 78,
    "hermione" : 99,
    "draco" : 74, 
    "neville" : 62,
}

student_grade = {}

for i in student_score:
    score = student_score[i]
    if score > 90 :
        student_grade[i] = "outstanding"
    elif score > 80 : 
        student_grade[i] = "Exeeds Expectation"
    elif score > 70 : 
        student_grade[i] = "Acceptable"
    else : 
        student_grade[i] = "Fail"

    
print(student_grade)