# Week 1 - Working with Lists and Dictionaries
# Goal:
# Collect and store student data using lists and dictionaries.
# Tasks:
# 1. Ask the user to input student details:
# - Name
# - Roll Number
# - Marks for 3 subjects: Math, Physics, Chemistry
student_data1={}
student_data2={}
student_data3={}
student_data4={}
students=[student_data1,student_data2,student_data3,student_data4]
for student in students:
    name = input('Enter your name : ')
    roll_no = input('Enter your roll_no : ')
    marks = eval(input('Enter marks for 3 subjects: Math, Physics, Chemistry as dictionary :'))
    student['name']=name
    student['roll_no']=roll_no
    student['marks']=marks



# 2. Store each student in a dictionary: Example:
# {
# "name": "John",
# "roll_no": "101",
# "marks": {"Math": 90, "Physics": 85, "Chemistry": 80}
# }



# 3. Append each student dictionary to a list.
student_list=[]
for student in students:
    student_list.append(student)

print(student_list)


# 4. Print all student data using a loop.
# Expected Output: Name: John
# Roll No: 101 Marks:

# Math: 90 Physics: 85 Chemistry: 80
# Concepts:
# - input()
# - dict and list
# - for loop and print formatting

for data in student_list:
    
    print(f'Name: {data['name']}\nRoll No: {data['roll_no']}\nMarks: \nMaths: {data['marks']['Math']}\nPhysics: {data['marks']['Physics']}\nChemistry: {data['marks']['Chemistry']}')
    print()

