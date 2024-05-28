import tkinter as tk
from tkinter import messagebox

# Function for adding a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to update the listbox with tasks
def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        task_listbox.insert(tk.END, f'{idx+1}. {task["task"]} - {status}')

# Function to mark a task as complete
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to update a task
def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks[selected_task_index]["task"] = new_task
            update_task_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task description.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

# Initialize the main window
root = tk.Tk()
root.title("To-Do List Application")

# Initialize the task list
tasks = []

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(root, width=70, height=15)
task_listbox.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

complete_button = tk.Button(button_frame, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()