import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)
    save_tasks()

def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        return

def mark_completed():
    try:
        index = task_listbox.curselection()[0]
        task = task_listbox.get(index)
        task_listbox.delete(index)
        task_listbox.insert(index, "✓ " + task)
        task_listbox.itemconfig(index, {'bg':'orchid1'})
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.configure(bg='plum2')

# Create title label
title_label = tk.Label(root, text="To-Do List", font=("dallas", 16, "bold"),bg='lightyellow')
title_label.pack(pady=10)

# Create task entry
task_entry = tk.Entry(root, width=40,bg='lightyellow')
task_entry.pack(pady=5)

# Create add button
add_button = tk.Button(root, text="Add Task", command=add_task,bg='white')
add_button.pack(pady=5)

# Create task listbox
task_listbox = tk.Listbox(root, width=50,bg='grey')
task_listbox.pack(pady=5)
load_tasks()

# Create remove button
remove_button = tk.Button(root, text="Remove Task", command=remove_task,bg='lightblue')
remove_button.pack(pady=5)

# Create mark as completed button
mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed,bg='lightgreen')
mark_button.pack(pady=5)

# Create clear all button
clear_button = tk.Button(root, text="Clear All", command=clear_tasks,bg='lightgray')
clear_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
