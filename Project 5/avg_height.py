student_heights = input("Input a list of students height ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)    
#total_height = sum(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
#number_of_students = len(student_heights)
number_of_students = 0
for studen in student_heights:
    number_of_students +=1
average_height = round(total_height/number_of_students)
print(average_height)