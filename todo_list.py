# A simple console-based To-Do List Application

# Task list to hold tasks
tasks = []

# Function to add a task
def add_task(task):
    if not task.strip():
        print("Error: Task cannot be empty.")  
        return
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")


