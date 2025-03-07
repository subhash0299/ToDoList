import tkinter as tk  # Import the Tkinter library for GUI development
from tkinter import messagebox  # Import messagebox for displaying pop-up alerts

# Define the ToDoList class
class ToDoList:
    def __init__(self, root):
        # Initialize the main window (root)
        self.root = root
        self.root.title('To-Do List')  # Set the title of the window
        self.root.geometry('400x450')  # Set the window size
        self.root.configure(bg='#E3F2FD')  # Set background color
        
        self.tasks = []  # List to store tasks
        
        # Create and pack the main label
        self.label = tk.Label(root, text="Welcome to To-Do List App", font=("Helvetica", 14, "bold"), bg='#E3F2FD')
        self.label.pack(pady=10)
        
        # Label for task entry
        self.label = tk.Label(root, text="Enter task:", font=("Helvetica", 12), bg='#E3F2FD')
        self.label.pack(pady=5)
        
        # Entry widget for user input
        self.enter_task = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.enter_task.pack(pady=5)
        
        # Button to add task
        self.add_button = tk.Button(root, text='Add Task', font=("Helvetica", 12, "bold"), fg='white', bg='#4CAF50', command=self.add_task)
        self.add_button.pack(pady=5)
        
        # Button to delete selected task
        self.delete_button = tk.Button(root, text='Delete Selected Task', font=("Helvetica", 12, "bold"), fg='white', bg='#F44336', command=self.delete_task)
        self.delete_button.pack(pady=5)
        
        # Listbox to display tasks
        self.task_list = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12), bg='white', fg='black', selectbackground='#FFEB3B')
        self.task_list.pack(pady=10)
    
    # Method to add a task to the list
    def add_task(self):
        task = self.enter_task.get()  # Get the task from entry widget
        if task:  # Check if task is not empty
            self.tasks.append(task)  # Add task to the list
            self.update_list()  # Update the listbox display
            self.enter_task.delete(0, tk.END)  # Clear the entry widget
        else:
            messagebox.showwarning("No Task Entered", "Please enter a task before adding.")  # Show warning
    
    # Method to delete a selected task
    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]  # Get the selected task index
            del self.tasks[task_index]  # Remove task from the list
            self.update_list()  # Update the listbox display
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task before deleting.")  # Show warning
    
    # Method to update the listbox with current tasks
    def update_list(self):
        self.task_list.delete(0, tk.END)  # Clear the listbox
        for task in self.tasks:  # Loop through tasks and add to listbox
            self.task_list.insert(tk.END, task)

# Run the Tkinter application
if __name__ == '__main__':
    root = tk.Tk()  # Create the main application window
    app = ToDoList(root)  # Instantiate the ToDoList class
    root.mainloop()  # Start the Tkinter event loop
