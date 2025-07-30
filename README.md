# todo-list-python
A simple CLI-based To-Do List app in Python
I recently developed a simple yet functional To-Do List application using Python. This project helped me strengthen my understanding of key programming concepts like:

🔹 User input handling
🔹 Conditional logic
🔹 Loops and lists
🔹 Menu-driven interfaces
🔹 Error handling

🛠️ The app allows users to:

Add new tasks

View current tasks

Delete tasks

Exit the program with clean prompts









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
