import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    try:
        listbox.delete(listbox.curselection())
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def save_tasks():
    try:
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for i in range(listbox.size()):
                f.write(listbox.get(i) + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Cannot save: {e}")

def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                task = line.strip()
                if task:
                    listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass  # First time running, no file yet
    except Exception as e:
        messagebox.showerror("Error", f"Cannot load: {e}")

# Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)
entry.bind("<Return>", lambda e: add_task())

# Buttons
tk.Button(root, text="Add Task", command=add_task, bg="green", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task, bg="red", fg="white", width=15).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 12), height=12, width=40)
listbox.pack(pady=10)

# Load saved tasks
load_tasks()

root.mainloop()
