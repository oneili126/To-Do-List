## To Do List

import tkinter as tk
from tkinter import messagebox

#color schemes
navy_blue = "#1e264c"
light_blue = "#87a6bb"
mustard = "#b99267"
coral = "#ae7268"
forest_green = "#154e52"
#Create the main window
window = tk.Tk()
window.title("To Do List App")
window.geometry("400x500")
window.config(bg="#1e264c")

#Create title label
title_label = tk.Label(window, text="To Do List", font=("Impact", 40))
title_label.pack(pady=10)
title_label.config(bg=navy_blue,fg=mustard)

#Create a list field for tasks
task_field = tk.Listbox(window, width=50, height=10)
task_field.pack(pady=10)
task_field.config(bg=light_blue)

#Create input line for add and edit task
task_input = tk.Entry(window, width=50)
task_input.pack(pady=5)
task_input.config(bg=light_blue)

#Create a dialogue box with instructions
messagebox.showinfo("Instructions", "The biggest box holds your To Do list. The text box under it is where you can type the items you wish to add to your to do list. To Add a Task: type in the text entry box, click add task. To remove a task: click on the task in your list and then click remove task. To edit a task: click the task you want to edit. Next, type the updates task in the text entry box. Then click edit task.")

#Create Buttons for adding, removing, and editing tasks
#Create a list to hold tasks
tasks = []

#Function to add a task
def add_task():
    task = task_input.get()
    if task:
        tasks.append(task)
        task_field.insert(tk.END, task)
        task_input.delete(0, tk.END)

#function to remove a task
def remove_task():
    selected = task_field.curselection()
    if selected:
        index = selected[0]
        task = task_field.get(index)
        if task in tasks:
            tasks.remove(task)
        task_field.delete(selected)

#function to edit a task
def edit_task():
    selected = task_field.curselection()
    if selected:
        index = selected[0]
        old_task = task_field.get(index)
        new_task = task_input.get()
        if old_task in tasks:
            tasks[index] = new_task
        task_field.delete(selected)
        task_field.insert(index,new_task)
        task_input.delete(0, tk.END)

add_task_button = tk.Button(window, text="Add Task", command=add_task)
add_task_button.config(bg = mustard)
add_task_button.pack(pady=5)
remove_task_button = tk.Button(window, text="Remove Task",command=remove_task)
remove_task_button.config(bg = coral)
remove_task_button.pack(pady=5)
edit_task_button = tk.Button(window, text="Edit Task",command=edit_task)
edit_task_button.config(bg = forest_green)
edit_task_button.pack(pady=5)

window.mainloop()
        
