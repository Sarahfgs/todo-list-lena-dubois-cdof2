# A simple console-based To-Do List Application

# Task list to hold tasks
tasks = []

# Function to add a task
def add_task():
    while True:  # Start an infinite loop
        task = input("Enter the task: ").strip()
        if not task:  # Check if the task is empty or whitespace
            print("Error: Task cannot be empty or whitespace. Please try again.")
        else:
            tasks.append({"task": task, "completed": False})  # Add valid task
            print(f"Task '{task}' added successfully!")
            break  # Exit the loop when a valid task is added



