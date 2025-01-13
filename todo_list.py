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

# Function to list all tasks
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

# Function to mark a task as completed
def mark_complete(index):
    # Check if the provided index is out of range
    if index < 0 or index >= len(tasks):  
        print("Error: Invalid task index.")  # Notify the user of an invalid index
        return
    # Mark the task at the given index as completed
    tasks[index]["completed"] = True
    # Notify the user of the successful update
    print(f"Task {index + 1} marked as completed!")  

# Function to delete a task
def delete_task(index):
    # Check if the provided index is out of range
    if index < 1 or index > len(tasks):  
        print("Error: Invalid task index.")  # Notify the user of an invalid index
        return
    # Remove the task at the given index
    tasks.pop(index)  
    # Notify the user of the successful deletion
    print(f"Task {index} deleted.")

# Main loop
def main():
    print("Welcome to the To-Do List Application!")
    while True:
        print("\nOptions:")
        print("1. Add a Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

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
                index = int(input("Enter the task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("Error: Please enter a valid task number.")
        elif choice == 5:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


