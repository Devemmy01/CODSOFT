import tkinter as tk
from tkinter import messagebox

def add_todo():
    todo = todo_entry.get()
    if todo:
        todos.append({"todo": todo, "completed": False})
        update_todo_listbox()
        todo_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a todo.")

def update_todo_listbox():
    todo_listbox.delete(0, tk.END)
    for idx, todo in enumerate(todos):
        status = "Completed" if todo["completed"] else "Not Completed"
        todo_listbox.insert(tk.END, f'{idx+1}. {todo["todo"]} - {status}')

def complete_todo():
    try:
        selected_todo_index = todo_listbox.curselection()[0]
        todos[selected_todo_index]["completed"] = True
        update_todo_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a todo to complete.")
        
def delete_todo():
    try:
        selected_todo_index = todo_listbox.curselection()[0]
        del todos[selected_todo_index]
        update_todo_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a todo to delete.")

def update_todo():
    try:
        selected_todo_index = todo_listbox.curselection()[0]
        new_todo = todo_entry.get()
        if new_todo:
            todos[selected_todo_index]["todo"] = new_todo
            update_todo_listbox()
            todo_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new todo description.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a todo to update.")

root = tk.Tk()
root.title("To-Do List Application")

todos = []

frame = tk.Frame(root)
frame.pack(pady=10)

todo_entry = tk.Entry(frame, width=50)
todo_entry.pack(side=tk.LEFT, padx=10)

add_btn = tk.Button(frame, text="Add todo", command=add_todo)
add_btn.pack(side=tk.LEFT)

todo_listbox = tk.Listbox(root, width=70, height=15)
todo_listbox.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

complete_btn = tk.Button(btn_frame, text="Complete todo", command=complete_todo)
complete_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(btn_frame, text="Delete todo", command=delete_todo)
delete_btn.pack(side=tk.LEFT, padx=10)

update_btn = tk.Button(btn_frame, text="Update todo", command=update_todo)
update_btn.pack(side=tk.LEFT, padx=10)
root.mainloop()