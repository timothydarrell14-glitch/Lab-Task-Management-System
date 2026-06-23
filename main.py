from task_manager.task_utils import (add_task, mark_task_as_complete, view_pending_tasks, calculate_progress)

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter title of Task").strip()
            description = input("Enter the description of the task").stip()
            due_date = input("Enter the due date of the task(YYYY-MM-DD)").strip
            add_task(title, description, due_date)
        elif choice == '2':
            mark_task_as_complete()
        elif choice == '3':
            view_pending_tasks()
        elif choice == '4':
            calculate_progress()
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
