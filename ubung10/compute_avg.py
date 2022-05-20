def compute_final_grades(students, grades):
    for i in range(len(students)):
        durch = sum(grades[i])/len(grades[i])
        students[i][1] = durch 
        
students = [["Joe", "-"], ["Kim", "-"], ["Sam", "-"]]
grades = [[5.0, 5.5, 4.5], [4.5, 4.0, 5.0],[3.5, 5.0, 6.0]]

compute_final_grades(students, grades)
print(students)
