import os
def generate_dummy_data():
    # Ensure the student_records directory exists
    os.makedirs('student_records', exist_ok=True)

    # Dummy Freshman data
    freshman_data = [
        "Emily Chen, 18, F001, 3.8, emily.chen@university.edu",
        "Jason Rodriguez, 19, F002, 3.5, jason.rodriguez@university.edu",
        "Sarah Thompson, 18, F003, 3.9, sarah.thompson@university.edu",
        "Michael Wong, 19, F004, 3.2, michael.wong@university.edu",
        "Olivia Patel, 18, F005, 4.0, olivia.patel@university.edu"
    ]

    # Dummy Sophomore data
    sophomore_data = [
        "Alex Kim, 20, S001, Computer Science, 3.6",
        "Emma Gonzalez, 20, S002, Biology, 3.8",
        "Ryan Nguyen, 19, S003, Engineering, 3.4",
        "Sophia Martinez, 20, S004, Psychology, 3.7",
        "Lucas Chen, 19, S005, Mathematics, 3.5"
    ]

    # Dummy Junior data
    junior_data = [
        "Ethan Park, 21, J001, Computer Science, 3.7, True, False",
        "Ava Sharma, 21, J002, Bioengineering, 3.6, False, True", 
        "Noah Williams, 22, J003, Electrical Engineering, 3.5, True, True",
        "Isabella Garcia, 21, J004, Environmental Science, 3.8, False, False",
        "Liam Thompson, 22, J005, Economics, 3.4, True, False"
    ]

    # Dummy Senior data
    senior_data = [
        "Daniel Lee, 22, SR001, Computer Science, 3.9, True, Graduate School",
        "Zoe Anderson, 23, SR002, Biology, 3.7, True, Medical School",
        "Ethan Rodriguez, 22, SR003, Engineering, 3.6, True, Industry Job",
        "Aria Chen, 23, SR004, Psychology, 3.8, True, Research Position",
        "Jackson Kim, 22, SR005, Business, 3.5, True, Startup Founder"
    ]

    # Write dummy data to files
    dummy_files = {
        'freshman.txt': freshman_data,
        'sophomore.txt': sophomore_data,
        'junior.txt': junior_data,
        'senior.txt': senior_data
    }

    for filename, data in dummy_files.items():
        with open(os.path.join('student_records', filename), 'w') as file:
            for line in data:
                file.write(line + '\n')

    print("Dummy data generated successfully!")

generate_dummy_data()    