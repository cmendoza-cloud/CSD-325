# Carmen Mendoza 
# Module 8.2 


import json

# Open the JSON file and load its contents
with open("students.json", "r") as file:
    students = json.load(file)  # Load the JSON data into a Python object (list of dictionaries)

# Print the loaded data
print(students)

# To access specific data or perform operations, use the 'students' variable
for student in students:
    print(f"Name: {student['F_Name']} {student['L_Name']}, Email: {student['Email']}")



[
    {
        "F_Name": "Ellen",
        "L_Name": "Ripley",
        "Student_ID": 45604,
        "Email": "eripley@gmail.com"
    },
    {
        "F_Name": "Arthur",
        "L_Name": "Dallas",
        "Student_ID": 45605,
        "Email": "adallas@gmail.com"
    },
    {
        "F_Name": "Joan",
        "L_Name": "Lambert",
        "Student_ID": 45714,
        "Email": "jlambert@gmail.com"
    },
    {
        "F_Name": "Thomas",
        "L_Name": "Kane",
        "Student_ID": 68554,
        "Email": "tkane@gmail.com"
    }
]

