class Student:
    student_count = 0

    def __init__(self, name, ID, age, email):
        self.name = name
        self.ID = ID
        self.age = age
        self.email = email
        Student.student_count += 1

    def display_student_information(self):
        print(f"""
        ---------------------------------      
        Name: {self.name}
        Student ID: {self.ID}
        Age: {self.age}
        Email: {self.email}
        """)    

    def update_student_information(self, name=None, ID=None, age=None, email=None):
        if name:
            self.name = name
        if ID:
            self.ID = ID
        if age:
            self.age = age
        if email:
            self.email = email
        print("Student information updated successfully.")

class Freshman(Student):
    freshman_count = 0

    def __init__(self, name, ID, age, email, high_school_gpa=None, major=None):
        super().__init__(name, ID, age, email)
        self.high_school_gpa = high_school_gpa
        self.orientation_completed = False
        self.major = major
        Freshman.freshman_count += 1

    def calculate_scholarship_eligibility(self):
        """
        Determine scholarship eligibility based on high school GPA
        Returns True if eligible, False otherwise
        """
        if self.high_school_gpa is None:
            return False
        
        if self.high_school_gpa >= 3.0:
            return True
        return False
    
    def complete_orientation(self):
        """
        Mark orientation as completed
        """
        self.orientation_completed = True
        print(f"{self.name} has completed freshman orientation.")

    def declare_major(self, major):
        """
        Declare a major for the student
        """
        if not self.major:
            self.major = major
            print(f"{self.name} has declared {major} as their major.")   
        else:
            print(f"Major already declared as {self.major}")         

class Sophomore(Student):
    sophomore_count = 0

    def __init__(self, name, ID, age, email, major, cumulative_gpa=None):
        super().__init__(name, ID, age, email)
        self.cumulative_gpa = cumulative_gpa
        self.major = major
        Sophomore.sophomore_count += 1

    def calculate_academic_standing(self):
        """
        Determine academic standing based on cumulative GPA
        """
        if self.cumulative_gpa is None:
            return "No GPA Available"
        
        if self.cumulative_gpa >= 3.5:
            return "Dean's List"
        elif self.cumulative_gpa >= 3.0:
            return "Good Standing"
        elif self.cumulative_gpa >= 2.0:
            return "Academic Warning"
        else:
            return "Academic Probation"

class Junior(Student):
    junior_count = 0

    def __init__(self, name, ID, age, email, major, cumulative_gpa=None):
        super().__init__(name, ID, age, email)
        self.cumulative_gpa = cumulative_gpa
        self.internship_status = False
        self.research_involvement = False
        self.major = major
        Junior.junior_count += 1

    def track_internship(self, internship_status):
        """
        Update internship status
        """
        self.internship_status = internship_status
        status = "started" if internship_status else "not started"
        print(f"{self.name}'s internship has {status}.")

    def calculate_credits_to_graduation(self, current_credits):
        """
        Calculate remaining credits for graduation
        Assumes 120 total credits needed
        """
        remaining_credits = 120 - current_credits
        return remaining_credits

class Senior(Student):
    senior_count = 0

    def __init__(self, name, ID, age, email, major, cumulative_gpa=None):
        super().__init__(name, ID, age, email)
        self.cumulative_gpa = cumulative_gpa
        self.graduation_requirements_met = False
        self.post_graduation_plans = None
        self.major = major
        Senior.senior_count += 1

    def verify_graduation_eligibility(self, total_credits, required_credits=120):
        """
        Check if student meets graduation requirements
        """
        if total_credits >= required_credits:
            self.graduation_requirements_met = True
            return True
        return False

    def set_post_graduation_plans(self, plans):
        """
        Set post-graduation plans
        """
        self.post_graduation_plans = plans
        print(f"{self.name}'s post-graduation plan: {plans}")

# Class for saving student details to a file
class SaveStudentDetails:
    def __init__(self, file_path):
        self.file_path = file_path

# Class for saving Freshman details
class SaveFreshmanDetails(SaveStudentDetails):
    def __init__(self, file_path, operation = 'a'):
        super().__init__(file_path)
        self.operation = operation

    def save(self, student: Freshman):
        with open(self.file_path, mode = self.operation) as file:
            student_info = f"{student.name}, {student.age}, {student.ID}, {student.high_school_gpa}, {student.email}\n"
            file.write(student_info)

# Class for saving Sophomore details
class SaveSophomoreDetails(SaveStudentDetails):
    def __init__(self, file_path, operation = 'a'):
        super().__init__(file_path)
        self.operation = operation

    def save(self, student: Sophomore):
        with open(self.file_path, mode = self.operation) as file:
            student_info = f"{student.name}, {student.age}, {student.ID}, {student.major}, {student.cumulative_gpa}\n"
            file.write(student_info)

# Class for saving Junior details
class SaveJuniorDetails(SaveStudentDetails):
    def __init__(self, file_path, operation = 'a'):
        super().__init__(file_path)
        self.operation = operation

    def save(self, student: Junior):
        with open(self.file_path, mode = self.operation) as file:
            student_info = f"{student.name}, {student.age}, {student.ID}, {student.major}, {student.cumulative_gpa}, {student.internship_status}, {student.research_involvement}\n"
            file.write(student_info)

# Class for saving Senior details
class SaveSeniorDetails(SaveStudentDetails):
    def __init__(self, file_path, operation = 'a'):
        super().__init__(file_path)
        self.operation = operation

    def save(self, student: Senior):
        with open(self.file_path, mode = self.operation) as file:
            student_info = f"{student.name}, {student.age}, {student.ID}, {student.major}, {student.cumulative_gpa}, {student.graduation_requirements_met}, {student.post_graduation_plans}\n"
            file.write(student_info)
