import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x400")  # Set the dimensions of the application window
        
        # Task List
        self.tasks = []

        # Task Entry
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add Task Button
        add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        add_button.pack(pady=5)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10, bg="#B3E0FF")  # Light blue background color
        self.task_listbox.pack(pady=10)

        # Task Finished Button
        finished_button = tk.Button(root, text="Task Finished", command=self.mark_complete, bg="#008CBA", fg="white")
        finished_button.pack(pady=5)

        # Delete Task Button
        delete_button = tk.Button(root, text="Delete Task", command=self.remove_task, bg="#f44336", fg="white")
        delete_button.pack(pady=5)

        # Clear All Button
        clear_all_button = tk.Button(root, text="Clear All", command=self.clear_all, bg="#FFD700", fg="black")  # Gold color
        clear_all_button.pack(pady=5)

        # Close App Button
        close_button = tk.Button(root, text="Close App", command=root.destroy, bg="#555", fg="white")
        close_button.pack(pady=5)

        # Set background color for the entire window
        root.configure(bg="#B3E0FF")  # Light blue background color

    def add_task(self):
        new_task = self.task_entry.get()
        if new_task:
            self.tasks.append((new_task, False))  # Use tuple to store task and completion status
            self.task_listbox.insert(tk.END, new_task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_complete(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_mark = self.tasks[selected_task_index[0]]
            if not task_to_mark[1]:  # Check if the task is not already marked as complete
                messagebox.showinfo("Task Finished", f"Task '{task_to_mark[0]}' marked as finished.")
                self.tasks[selected_task_index[0]] = (task_to_mark[0], True)  # Update completion status
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(tk.END, f"{task_to_mark[0]} (✔)")
            else:
                messagebox.showinfo("Task Finished", f"Task '{task_to_mark[0]}' is already marked as finished.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as finished.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_remove = self.tasks[selected_task_index[0]]
            self.tasks.remove(task_to_remove)
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
    
    def clear_all(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
