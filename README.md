This project is a Student Management System designed with a GUI built using Python's tkinter. It manages student records across different academic levels (Freshman, Sophomore, Junior, Senior), enabling users to add, update, delete, and save student details. Each student type has specific attributes (e.g., GPA, major, internship status) and methods (e.g., scholarship eligibility, academic standing). Data persistence is handled through file-based storage, with separate files for each student type stored in a student_records directory.



Detailed Algorithm for Student Management System

1. Initialize the Application:
   - Launch the tkinter GUI with a main window titled "Student Management System".
   - Check for existing student data files in the directory "student_records".
     - For each student type file (e.g., "freshman.txt"), open the file.
     - Parse each line to reconstruct student objects and add them to the system's internal list.
   - Populate the Treeview with the parsed student data.

2. GUI Setup:
   - Create dropdown menu for selecting student type (Freshman, Sophomore, Junior, Senior).
     - Bind an event listener to dynamically update additional fields based on the selected type.
   - Common input fields include Name, ID, Age, and Email.
   - Additional input fields depend on the selected student type:
     - Freshman: High School GPA, Major.
     - Sophomore: Major, Cumulative GPA.
     - Junior: Major, Cumulative GPA, Internship Status.
     - Senior: Major, Cumulative GPA, Graduation Requirements.

   - Buttons and their functionalities:
     - Add Student: Create and add a new student to the system.
     - Update Student: Modify attributes of an existing student.
     - Delete Student: Remove a student from both the Treeview and the internal list.
     - Save Details: Save all students' data to their respective files.

   - Treeview setup:
     - Display student data in a tabular format with columns for Name, ID, and Type.
     - Enable selection to allow users to edit or delete a specific student's record.

3. Adding a Student:
   - Retrieve input data from common and additional fields.
   - Validate input to ensure completeness and correctness.
   - Based on the selected type, create an instance of the appropriate student class (Freshman, Sophomore, etc.).
   - Append the created object to the internal list of students.
   - Add the student to the Treeview with their Name, ID, and Type displayed.
   - Clear input fields to prepare for the next entry.

4. Updating a Student:
   - Ensure a student is selected in the Treeview; show an error message if none is selected.
   - Retrieve the selected student's ID and locate the corresponding object in the internal list.
   - Update the object's attributes using the input fields.
   - Update the Treeview to reflect the changes.
   - Display a success message indicating the update was completed.

5. Deleting a Student:
   - Ensure a student is selected in the Treeview; show an error message if none is selected.
   - Retrieve the selected student's ID and remove the corresponding object from the internal list.
   - Remove the selected entry from the Treeview.
   - Update the corresponding text file by rewriting it without the deleted student's record.
   - Display a success message indicating the deletion was successful.

6. Saving Student Details:
   - For each student type (Freshman, Sophomore, Junior, Senior), create or open the corresponding text file in the "student_records" directory.
   - Iterate through the internal list of students and save their details to their respective files using the appropriate format.
   - Display a confirmation message indicating that the details were saved successfully.

7. Handling Data Persistence:
   - On application start-up:
     - Check for the presence of "student_records" directory.
     - If student files exist, read and parse them to reconstruct student objects.
     - Populate the Treeview with the reconstructed data for user visibility.
   - On data modifications (Add, Update, Delete):
     - Immediately update the internal list of students and the Treeview.
     - Save changes to the appropriate text file when the "Save Details" button is clicked.

8. Planned Enhancements:
   - Implement a file-based password system for securing access to the application.
     - Use a hashed password stored in a separate file to validate user credentials at login.
   - Extend data retrieval functionality to include error handling for corrupt or missing files.
     - Ensure that the application gracefully handles empty files or formatting issues.

Classes Overview:
1. Student (Base Class):
   - Attributes: name, ID, age, email.
   - Methods: display_student_information, update_student_information.

2. Freshman:
   - Attributes: high_school_gpa, major, orientation_completed.
   - Methods: calculate_scholarship_eligibility, complete_orientation.

3. Sophomore:
   - Attributes: major, cumulative_gpa.
   - Methods: calculate_academic_standing.

4. Junior:
   - Attributes: major, cumulative_gpa, internship_status, research_involvement.
   - Methods: track_internship, calculate_credits_to_graduation.

5. Senior:
   - Attributes: major, cumulative_gpa, graduation_requirements_met, post_graduation_plans.
   - Methods: verify_graduation_eligibility, set_post_graduation_plans.

6. SaveStudentDetails and Subclasses:
   - Handles saving student data to files based on type.

Conclusion:
The final build of the application will include robust data persistence, ensuring all student details are loaded at startup and stored securely upon modifications. A password system will protect access, adding a layer of security to the management system.
