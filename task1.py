# Week 1 - Working with Lists and Dictionaries
# Goal:
# Collect and store student data using lists and dictionaries.
# Tasks:
# 1. Ask the user to input student details:
# - Name
# - Roll Number
# - Marks for 3 subjects: Math, Physics, Chemistry

name = input('Enter your name : ')
roll_no = input('Enter your roll_no : ')
marks = eval(input('Enter marks for 3 subjects: Math, Physics, Chemistry as dictionary :'))



# 2. Store each student in a dictionary: Example:
# {
# "name": "John",
# "roll_no": "101",
# "marks": {"Math": 90, "Physics": 85, "Chemistry": 80}
# }
student_data={}
student_data['name']=name
student_data['roll_no']=roll_no
student_data['marks']=marks

# 3. Append each student dictionary to a list.
student_list=[]
student_list.append(student_data)

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

