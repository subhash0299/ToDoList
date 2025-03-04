import tkinter as tk
from tkinter import messagebox

#create class

class ToDoList:

    def __init__(self, root):
        self.root = root
        self.root.title('To Do List')
        self.root.geometry('400x400')

        self.tasks = []

        self.label = tk.Label(root, text= "Hello Welcome to To Do List app")
        self.label.pack(pady = 10)

        self.label = tk.Label(root, text="Enter task to add ")
        self.label.pack(pady=10)

        self.enter_task = tk.Entry(root, width=40)
        self.enter_task.pack(pady = 5)

        self.add_button = tk.Button(root, text= 'Add Task', fg='red', bg='white', command=self.add_task)
        self.add_button.pack(pady = 5)

        self.delete_button = tk.Button(root, text='Delete Selected Task', fg='red', bg='white', command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=40, height= 10, bg='yellow')
        self.task_list.pack(pady = 10)





    def add_task(self):
        task = self.enter_task.get()
        if task !="":
            self.tasks.append(task)
            self.update_list()
            self.enter_task.delete(0,tk.END)
        else:
            messagebox.showwarning("no tasks ","Enter task first")


    def delete_task(self):
        try:
            task_index = self.task_list.curselection()
            selected_task = self.task_list.get(task_index)
            self.tasks.remove(selected_task)
            self.update_list()
        except :
            messagebox.showwarning('no selection', "select task before deleting")


    def update_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)




if __name__ == '__main__':

    r = tk.Tk()

    app = ToDoList(r)

    tk.mainloop()
