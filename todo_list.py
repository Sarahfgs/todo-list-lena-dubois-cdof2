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

def list_tasks():
    # Check if the task list is empty
    if len(tasks) == 0:
        print("No tasks available!")
        return []

    task_list = []
    # Iterate over tasks with 1-based numbering
    for index, task in enumerate(tasks, start=1):
        # Format the task with its status
        status = "✔" if task["completed"] else "✘"
        task_str = f"{index}. {task['task']} [{status}]"
        print(task_str)
        task_list.append(task_str)
    return task_list


