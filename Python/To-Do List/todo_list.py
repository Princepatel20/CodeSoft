# Define a list to store tasks
tasks = []

def show_menu():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def update_task():
    view_tasks()
    index = int(input("Enter the index of the task to update: "))
    if index >= 1 and index <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[index - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid index!")

def delete_task():
    view_tasks()
    index = int(input("Enter the index of the task to delete: "))
    if index >= 1 and index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' has been deleted.")
    else:
        print("Invalid index!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
