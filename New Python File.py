import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_all_tasks():
    task_listbox.delete(0, tk.END)


root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x500")


heading_label = tk.Label(root, text="To-Do List", font=("Arial", 16), fg="white", bg="blue", pady=10)
heading_label.pack(fill=tk.X)


task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_entry = tk.Entry(task_frame, width=30, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, padx=10)

add_task_button = tk.Button(task_frame, text="Add Task", command=add_task, bg="green", fg="white", font=("Arial", 10))
add_task_button.pack(side=tk.LEFT)


task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="red", fg="white", font=("Arial", 10))
delete_task_button.pack(side=tk.LEFT, padx=10)

clear_all_button = tk.Button(button_frame, text="Clear All", command=clear_all_tasks, bg="orange", fg="white", font=("Arial", 10))
clear_all_button.pack(side=tk.LEFT, padx=10)


root.mainloop()
