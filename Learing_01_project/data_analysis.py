import json

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

student_data = load_data('data02.json')

# target hestags for target students
python_hestag = 3
data_science_hestag = [1, 3]
web_develpers_hestag = [2,4,5,11]


# Find Data science student
def data_science_student():
    print("Data science students:")
    print("-"*25)
    for student in student_data['student']:
        liked = student['liked_pages_hestag']
    
        if (tag in liked for tag in data_science_hestag):
            print(f"Student_name: {student['name']}\nStudent_coures: {student['coures']} {student['sem']}sem\nStudent_Insta_id: {student['inst_id']}")
            print("-"*25)
    else:
        print("No more students")
        print(" ")


# Find Website develper student
def website_develper_student():
    print("Website develpment student")
    print("-"*25)
    for student in student_data['student']:
        liked = student['liked_pages_hestag']

        if (tag in liked for tag in web_develpers_hestag):
            print(f"Student_name: {student['name']}\nStudent_coures: {student['coures']} {student['sem']}sem\nStudent_Insta_id: {student['inst_id']}")
            print("-"*25)
    else:
        print("No more students")
        print(" ")


# find python students
def python_student():
    print("Python students:")
    print("-"*25)
    for student in student_data['student']:
        if python_hestag in student['liked_pages_hestag']:
            print(f"Student_name: {student['name']}\nStudent_coures: {student['coures']} {student['sem']}sem\nStudent_Insta_id: {student['inst_id']}")
            print("-"*25)
    else:
        print("No more students")
        print(" ")


python_student()
data_science_student()
website_develper_student()