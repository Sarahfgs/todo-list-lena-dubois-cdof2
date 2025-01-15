# A simple console-based To-Do List Application

# Task list to hold tasks
tasks = []

# Function to add a task
def add_task():
    while True:
        task = input("Enter the task: ").strip()
        if not task:
            print("Error: Task cannot be empty or whitespace. Please try again.")
        else:
            tasks.append({"task": task, "completed": False})
            print(f"Task '{task}' added successfully!")
            break

# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks available!")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. {task['task']} [{status}]")

# Function to mark a task as completed
def mark_complete(index):
    if index < 1 or index > len(tasks):
        print("Error: Invalid task index.")
        return
    tasks[index - 1]["completed"] = True
    print(f"Task {index} marked as completed!")

# Function to delete a task
def delete_task(index):
    if index < 1 or index > len(tasks):
        print("Error: Invalid task index.")
        return
    removed_task = tasks.pop(index - 1)
    print(f"Task '{removed_task['task']}' deleted.")

# Function to edit a task
def edit_task():
    if not tasks:
        print("No tasks available to edit!")
        return

    list_tasks()
    try:
        task_number = int(input("\nEnter the task number you want to edit: "))
        if task_number < 1 or task_number > len(tasks):
            print("Error: Invalid task number.")
            return

        new_task = input("Enter the new task description: ").strip()
        if new_task:
            tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated successfully!")
        else:
            print("Error: Task description cannot be empty.")
    except ValueError:
        print("Error: Please enter a valid task number.")

# Main loop
def main():
    print("Welcome to the To-Do List Application!")
    while True:
        print("\nOptions:")
        print("1. Add a Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Edit Task")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Error: Please enter a number.")
            continue

        if choice == 1:
            add_task()
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            try:
                index = int(input("Enter the task number to mark as complete: "))
                mark_complete(index)
            except ValueError:
                print("Error: Please enter a valid task number.")
        elif choice == 4:
            try:
                index = int(input("Enter the task number to delete: "))
                delete_task(index)
            except ValueError:
                print("Error: Please enter a valid task number.")
        elif choice == 5:
            edit_task()
        elif choice == 6:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
