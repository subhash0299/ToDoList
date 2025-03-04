import tkinter as tk
from tkinter import messagebox

# Create class
class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('400x450')
        self.root.configure(bg='#E3F2FD')  # Light blue background

        self.tasks = []

        self.label = tk.Label(root, text="Welcome to To-Do List App", font=("Helvetica", 14, "bold"), bg='#E3F2FD')
        self.label.pack(pady=10)

        self.label = tk.Label(root, text="Enter task:", font=("Helvetica", 12), bg='#E3F2FD')
        self.label.pack(pady=5)

        self.enter_task = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.enter_task.pack(pady=5)

        self.add_button = tk.Button(root, text='Add Task', font=("Helvetica", 12, "bold"), fg='white', bg='#4CAF50', command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text='Delete Selected Task', font=("Helvetica", 12, "bold"), fg='white', bg='#F44336', command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12), bg='white', fg='black', selectbackground='#FFEB3B')
        self.task_list.pack(pady=10)

    def add_task(self):
        task = self.enter_task.get()
        if task:
            self.tasks.append(task)
            self.update_list()
            self.enter_task.delete(0, tk.END)
        else:
            messagebox.showwarning("No Task Entered", "Please enter a task before adding.")

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            del self.tasks[task_index]
            self.update_list()
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task before deleting.")

    def update_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
