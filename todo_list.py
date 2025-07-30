def main():
    task = []
    
todo_list = []
while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == '2':
        print("Your Tasks:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

    elif choice == '3':
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("Exiting the To-do list.")
        break

    else:
        print("Invalid choice. Please try again.")
