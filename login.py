import tkinter as tk
from tkinter import ttk, messagebox
import os
import re

class LoginInterface:
    def __init__(self, master):
        self.master = master
        master.title("Student Management System - Login")
        master.geometry("500x700")
        master.configure(bg='#f0f0f0')

        # Configure style
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TButton', font=('Arial', 12))

        # Create main frame
        self.main_frame = ttk.Frame(master, padding="30 30 30 30")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Logo or Title
        self.create_header()

        # Login Fields
        self.create_login_fields()

        # Error Label
        self.error_label = ttk.Label(self.main_frame, text="", foreground='red', 
                                     style='TLabel', wraplength=300)
        self.error_label.pack(pady=(10, 20))

        # Login Button
        self.create_login_button()

        # Create User Section
        self.create_user_section()

        # Set default credentials
        self.default_user_name = 'admin'
        self.default_password = 'password'

    def create_header(self):
        # Create a stylish header
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(pady=(0, 30))

        # Application Title
        title_label = ttk.Label(header_frame, text="Student Management System", 
                                font=('Arial', 16, 'bold'), 
                                foreground='#333333')
        title_label.pack()

        subtitle_label = ttk.Label(header_frame, text="Secure Login", 
                                   font=('Arial', 12), 
                                   foreground='#666666')
        subtitle_label.pack()

    def create_login_fields(self):
        # Username Field
        username_frame = ttk.Frame(self.main_frame)
        username_frame.pack(fill=tk.X, pady=(0, 10))

        username_label = ttk.Label(username_frame, text="Username:", style='TLabel')
        username_label.pack(anchor='w')

        self.username_entry = ttk.Entry(username_frame, width=40, 
                                        font=('Arial', 12))
        self.username_entry.pack(fill=tk.X)

        # Password Field
        password_frame = ttk.Frame(self.main_frame)
        password_frame.pack(fill=tk.X, pady=(0, 20))

        password_label = ttk.Label(password_frame, text="Password:", style='TLabel')
        password_label.pack(anchor='w')

        self.password_entry = ttk.Entry(password_frame, width=40, 
                                        show="*", font=('Arial', 12))
        self.password_entry.pack(fill=tk.X)

        # Bind Enter key to login
        self.password_entry.bind('<Return>', self.check_matches)

    def create_login_button(self):
        # Styled Login Button
        login_button = ttk.Button(self.main_frame, text="Sign In", 
                                  command=self.check_matches,
                                  style='Accent.TButton')
        login_button.pack(fill=tk.X, pady=(10, 0))

        # Configure a custom button style
        self.style.configure('Accent.TButton', 
                             background='#4CAF50', 
                             foreground='white', 
                             font=('Arial', 12, 'bold'))
        self.style.map('Accent.TButton', 
                       background=[('active', '#45a049')])

    def create_user_section(self):
        # Separator
        ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=20)

        # Create User Label
        create_user_label = ttk.Label(self.main_frame, text="Create New User", 
                                      font=('Arial', 14, 'bold'), 
                                      foreground='#333333')
        create_user_label.pack(pady=(0, 10))

        # New Username Field
        new_username_frame = ttk.Frame(self.main_frame)
        new_username_frame.pack(fill=tk.X, pady=(0, 10))

        new_username_label = ttk.Label(new_username_frame, text="New Username:", style='TLabel')
        new_username_label.pack(anchor='w')

        self.new_username_entry = ttk.Entry(new_username_frame, width=40, 
                                            font=('Arial', 12))
        self.new_username_entry.pack(fill=tk.X)

        # New Password Field
        new_password_frame = ttk.Frame(self.main_frame)
        new_password_frame.pack(fill=tk.X, pady=(0, 10))

        new_password_label = ttk.Label(new_password_frame, text="New Password:", style='TLabel')
        new_password_label.pack(anchor='w')

        self.new_password_entry = ttk.Entry(new_password_frame, width=40, 
                                            show="*", font=('Arial', 12))
        self.new_password_entry.pack(fill=tk.X)

        # Confirm Password Field
        confirm_password_frame = ttk.Frame(self.main_frame)
        confirm_password_frame.pack(fill=tk.X, pady=(0, 20))

        confirm_password_label = ttk.Label(confirm_password_frame, text="Confirm Password:", style='TLabel')
        confirm_password_label.pack(anchor='w')

        self.confirm_password_entry = ttk.Entry(confirm_password_frame, width=40, 
                                                show="*", font=('Arial', 12))
        self.confirm_password_entry.pack(fill=tk.X)

        # Create User Button
        create_user_button = ttk.Button(self.main_frame, text="Create User", 
                                        command=self.create_new_user,
                                        style='Create.TButton')
        create_user_button.pack(fill=tk.X, pady=(10, 0))

        # Configure create user button style
        self.style.configure('Create.TButton', 
                             background='#2196F3', 
                             foreground='white', 
                             font=('Arial', 12, 'bold'))
        self.style.map('Create.TButton', 
                       background=[('active', '#1976D2')])

    def check_matches(self, event=None):
        entered_username = self.username_entry.get()
        entered_password = self.password_entry.get()
        
        # Ensure credentials files exist
        self.ensure_credentials_files()

        # Read saved credentials
        saved_user_names, saved_passwords = self.read_credentials()

        try:
            line_of_given_username = saved_user_names.index(entered_username)
            line_of_given_password = saved_passwords.index(entered_password)
            
            if line_of_given_username == line_of_given_password:
                self.master.destroy()
                root = tk.Tk()
                from ManagementSystem import StudentManagementGUI
                StudentManagementGUI(root)
            else:
                self.error_label.config(text="Invalid username or password.")
        except ValueError:
            self.error_label.config(text="Invalid username or password.")
        
        # Clear entries
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def create_new_user(self):
        # Get new user details
        new_username = self.new_username_entry.get().strip()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Validate input
        if not new_username:
            messagebox.showerror("Error", "Username cannot be empty")
            return

        if len(new_username) < 4:
            messagebox.showerror("Error", "Username must be at least 4 characters long")
            return

        if not re.match("^[a-zA-Z0-9_]+$", new_username):
            messagebox.showerror("Error", "Username can only contain letters, numbers, and underscores")
            return

        if len(new_password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        # Check if username already exists
        saved_user_names, _ = self.read_credentials()
        if new_username in saved_user_names:
            messagebox.showerror("Error", "Username already exists")
            return

        # Add new user
        try:
            with open('usernames.txt', 'a') as user_file:
                user_file.write(f"\n{new_username}")
            
            with open('passwords.txt', 'a') as pass_file:
                pass_file.write(f"\n{new_password}")

            messagebox.showinfo("Success", "User created successfully!")

            # Clear entries
            self.new_username_entry.delete(0, tk.END)
            self.new_password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to create user: {str(e)}")

    def ensure_credentials_files(self):
        if not (os.path.exists('usernames.txt') and os.path.exists('passwords.txt')):
            # Create default files
            with open('usernames.txt', 'w') as file:
                file.write(self.default_user_name)
            with open('passwords.txt', 'w') as file:
                file.write(self.default_password)

    def read_credentials(self):
        with open('usernames.txt', 'r') as file:
            saved_user_names = file.read().splitlines()
        with open('passwords.txt', 'r') as file:
            saved_passwords = file.read().splitlines()
        return saved_user_names, saved_passwords

def main():
    root = tk.Tk()
    app = LoginInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()