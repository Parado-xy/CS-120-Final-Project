import tkinter as tk
from tkinter import ttk, messagebox
import os
from StudentClasses import Freshman, Sophomore, Junior, Senior, SaveFreshmanDetails, SaveSophomoreDetails, SaveJuniorDetails, SaveSeniorDetails

# Save each student type to a separate file
student_types = {
    'Freshman': SaveFreshmanDetails('student_records/freshman.txt'),
    'Sophomore': SaveSophomoreDetails('student_records/sophomore.txt'),
    'Junior': SaveJuniorDetails('student_records/junior.txt'),
    'Senior': SaveSeniorDetails('student_records/senior.txt')
}

os.listdir()


class StudentManagementGUI:
    

    def __init__(self, master):
        self.master = master
        master.title("Student Management System")
        master.geometry("800x600")

        # Student type selection
        self.student_type_var = tk.StringVar(value="Freshman")
        self.student_type_label = ttk.Label(master, text="Select Student Type:")
        self.student_type_label.pack(pady=10)

        student_types = ["Freshman", "Sophomore", "Junior", "Senior"]
        self.student_type_dropdown = ttk.Combobox(master, textvariable=self.student_type_var, 
                                                   values=student_types, state="readonly")
        self.student_type_dropdown.pack(pady=5)

        # Input Frames
        self.create_input_frames(master)

        # Buttons
        self.create_buttons(master)

        # Student List
        self.create_student_list(master)

        # Initialize student storage
        self.students = []

        # Load up students already in database.
        self.load_students_from_files()

    def load_students_from_files(self):
        # Clear existing students
        self.students.clear()
        
        # Ensure the student_records directory exists
        if not os.path.exists('student_records'):
            return

        # Define loading methods for each student type
        def load_freshman(line):
            try:
                name, age, ID, high_school_gpa, email = line.strip().split(', ')
                return Freshman(name, ID, int(age), email, float(high_school_gpa), None)
            except ValueError:
                print(f"Error parsing Freshman line: {line}")
                return None

        def load_sophomore(line):
            try:
                name, age, ID, major, cumulative_gpa = line.strip().split(', ')
                return Sophomore(name, ID, int(age), "", major, float(cumulative_gpa))
            except ValueError:
                print(f"Error parsing Sophomore line: {line}")
                return None

        def load_junior(line):
            try:
                name, age, ID, major, cumulative_gpa, internship_status, research_involvement = line.strip().split(', ')
                junior = Junior(name, ID, int(age), "", major, float(cumulative_gpa))
                junior.internship_status = internship_status == 'True'
                junior.research_involvement = research_involvement == 'True'
                return junior
            except ValueError:
                print(f"Error parsing Junior line: {line}")
                return None

        def load_senior(line):
            try:
                name, age, ID, major, cumulative_gpa, graduation_requirements_met, post_graduation_plans = line.strip().split(', ')
                senior = Senior(name, ID, int(age), "", major, float(cumulative_gpa))
                senior.graduation_requirements_met = graduation_requirements_met == 'True'
                senior.post_graduation_plans = post_graduation_plans if post_graduation_plans != 'None' else None
                return senior
            except ValueError:
                print(f"Error parsing Senior line: {line}")
                return None

        # Mapping of file names to loading functions
        student_loaders = {
            'freshman.txt': load_freshman,
            'sophomore.txt': load_sophomore,
            'junior.txt': load_junior,
            'senior.txt': load_senior
        }

        # Iterate through each file and load students
        for filename, loader in student_loaders.items():
            file_path = os.path.join('student_records', filename)
            
            if not os.path.exists(file_path):
                continue

            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        if line.strip():  # Ignore empty lines
                            student = loader(line)
                            if student:
                                self.students.append(student)
                                # Also add to treeview
                                self.tree.insert("", tk.END, values=(
                                    student.name, 
                                    student.ID, 
                                    type(student).__name__
                                ))
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    

    def create_input_frames(self, master):
        # Common fields frame
        self.common_frame = ttk.Frame(master)
        self.common_frame.pack(pady=10)

        labels = ["Name:", "ID:", "Age:", "Email:"]
        self.common_entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self.common_frame, text=label).grid(row=0, column=i*2, padx=5)
            entry = ttk.Entry(self.common_frame, width=20)
            entry.grid(row=0, column=i*2+1, padx=5)
            self.common_entries[label.lower().strip(':')] = entry

        # Additional fields frame
        self.additional_frame = ttk.Frame(master)
        self.additional_frame.pack(pady=10)

        self.additional_entries = {}
        self.additional_labels = {
            "Freshman": ["High School GPA:", "Major:"],
            "Sophomore": ["Major:", "Cumulative GPA:"],
            "Junior": ["Major:", "Cumulative GPA:"],
            "Senior": ["Major:", "Cumulative GPA:"]
        }

        # Bind dropdown to update additional fields
        self.student_type_dropdown.bind('<<ComboboxSelected>>', self.update_additional_fields)
        self.update_additional_fields()

    def update_additional_fields(self, event=None):
        # Clear existing additional fields
        for widget in self.additional_frame.winfo_children():
            widget.destroy()

        student_type = self.student_type_var.get()
        labels = self.additional_labels.get(student_type, [])
        
        self.additional_entries.clear()
        for i, label in enumerate(labels):
            ttk.Label(self.additional_frame, text=label).grid(row=0, column=i*2, padx=5)
            entry = ttk.Entry(self.additional_frame, width=20)
            entry.grid(row=0, column=i*2+1, padx=5)
            self.additional_entries[label.lower().strip(':')] = entry

    def create_buttons(self, master):
        button_frame = ttk.Frame(master)
        button_frame.pack(pady=10)

        buttons = [
            ("Add Student", self.add_student),
            ("Update Student", self.update_student),
            ("Delete Student", self.delete_student),
            ("Save Details", self.save_student_details)
        ]

        for text, command in buttons:
            ttk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)

    def create_student_list(self, master):
        self.tree = ttk.Treeview(master, columns=("Name", "ID", "Type"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type")
        self.tree.pack(pady=10, expand=True, fill=tk.BOTH)

        # Bind selection event
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item[0])
            student_id = item['values'][1]
            selected_student = next((s for s in self.students if s.ID == student_id), None)
            
            if selected_student:
                # Populate fields with selected student's details
                self.populate_student_fields(selected_student)

    def populate_student_fields(self, student):
        # Reset fields first
        for entry in self.common_entries.values():
            entry.delete(0, tk.END)
        
        # Populate common fields
        self.common_entries['name'].insert(0, student.name)
        self.common_entries['id'].insert(0, student.ID)
        self.common_entries['age'].insert(0, str(student.age))
        self.common_entries['email'].insert(0, student.email)

        # Set student type
        student_type = type(student).__name__
        self.student_type_var.set(student_type)
        self.update_additional_fields()

        # Populate additional fields based on student type
        if student_type == 'Freshman':
            if hasattr(student, 'high_school_gpa') and student.high_school_gpa is not None:
                self.additional_entries['high school gpa'].insert(0, str(student.high_school_gpa))
            if hasattr(student, 'major') and student.major is not None:
                self.additional_entries['major'].insert(0, student.major)
        elif student_type in ['Sophomore', 'Junior', 'Senior']:
            if hasattr(student, 'major') and student.major is not None:
                self.additional_entries['major'].insert(0, student.major)
            if hasattr(student, 'cumulative_gpa') and student.cumulative_gpa is not None:
                self.additional_entries['cumulative gpa'].insert(0, str(student.cumulative_gpa))

    def add_student(self):
        try:
            # Get common fields
            name = self.common_entries['name'].get()
            id_num = self.common_entries['id'].get()
            age = int(self.common_entries['age'].get())
            email = self.common_entries['email'].get()

            # Get student type and create appropriate student object
            student_type = self.student_type_var.get()
            
            if student_type == 'Freshman':
                high_school_gpa = float(self.additional_entries.get('high school gpa', tk.StringVar()).get() or 0)
                major = self.additional_entries.get('major', tk.StringVar()).get()
                student = Freshman(name, id_num, age, email, high_school_gpa, major)
            elif student_type == 'Sophomore':
                major = self.additional_entries['major'].get()
                cumulative_gpa = float(self.additional_entries['cumulative gpa'].get() or 0)
                student = Sophomore(name, id_num, age, email, major, cumulative_gpa)
            elif student_type == 'Junior':
                major = self.additional_entries['major'].get()
                cumulative_gpa = float(self.additional_entries['cumulative gpa'].get() or 0)
                student = Junior(name, id_num, age, email, major, cumulative_gpa)
            elif student_type == 'Senior':
                major = self.additional_entries['major'].get()
                cumulative_gpa = float(self.additional_entries['cumulative gpa'].get() or 0)
                student = Senior(name, id_num, age, email, major, cumulative_gpa)
            
            # Add to students list and treeview
            self.students.append(student)
            self.tree.insert("", tk.END, values=(name, id_num, student_type))
            
            messagebox.showinfo("Success", f"{student_type} student added successfully!")
            
            # Clear input fields
            for entry in list(self.common_entries.values()) + list(self.additional_entries.values()):
                entry.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")

    def update_student(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to update")
            return

        try:
            # Get current student details
            item = self.tree.item(selected_item[0])
            current_id = item['values'][1]
            student = next((s for s in self.students if s.ID == current_id), None)

            if student:
                # Update common fields
                student.name = self.common_entries['name'].get()
                student.ID = self.common_entries['id'].get()
                student.age = int(self.common_entries['age'].get())
                student.email = self.common_entries['email'].get()

                # Update additional fields based on student type
                student_type = type(student).__name__
                if student_type == 'Freshman':
                    student.high_school_gpa = float(self.additional_entries.get('high school gpa', tk.StringVar()).get() or 0)
                    student.major = self.additional_entries.get('major', tk.StringVar()).get()
                elif student_type in ['Sophomore', 'Junior', 'Senior']:
                    student.major = self.additional_entries['major'].get()
                    student.cumulative_gpa = float(self.additional_entries['cumulative gpa'].get() or 0)

                # Update treeview
                self.tree.item(selected_item[0], values=(student.name, student.ID, student_type))
                
                messagebox.showinfo("Success", "Student information updated!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
    # FLAG: : : : : : : : : : : : : : :
    def delete_student(self):

        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a student to delete")
            return

        # Get student ID
        item = self.tree.item(selected_item[0])
        student_id = item['values'][1]
        student_type = item['values'][2]  # Get student type from treeview

        # Remove from students list
        self.students = [s for s in self.students if s.ID != student_id]
        
        # Remove from treeview
        self.tree.delete(selected_item[0])

        # Clear the corresponding file and re-save remaining students
        try:
            with open(f'student_records/{student_type.lower()}.txt', 'w') as file:
                file.write('')  # Clear the file
            
            # Save remaining students of the same type
            saver = student_types.get(student_type)
            if saver:
                for student in self.students:
                    if type(student).__name__ == student_type:
                        saver.save(student)

            messagebox.showinfo("Success", "Student deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete student: {str(e)}")

    def save_student_details(self):
        if not self.students:
            messagebox.showwarning("Warning", "No students to save!")
            return

        # Create directory if it doesn't exist
        os.makedirs('student_records', exist_ok=True)
        global student_types

        for student in self.students:
            student_type = type(student).__name__
            saver = student_types.get(student_type)
            if saver:
                saver.save(student)

        messagebox.showinfo("Success", "Student details saved to files!")

def main():
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()


# TODO: Update the delete Method to remove a deleted entry from file.
# TODO: Update app to acces files on start up and render such objects to the GUI.   
# TODO: For the delete method, we can improve things by using a central count variable in the sub student classes as a kind of primary key 

if __name__ == "__main__":
    main()