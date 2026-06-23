from datetime import datetime

# Import validation functions
from task_manager.validation import (validate_due_date,validate_task_description, validate_task_title,)

# Define tasks list
task = {"title": "Groceries",
 "description": "Shop at Market Basket for food", 
 "due_date": "2024-06-26",
 "completed": True}

# Implement add_task function
def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task.append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    })
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete():
    # task = tasks[index]
    # task['completed'] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks = task):
    for task in tasks:
        if task['completed'] == False:
            print(task)

# Implement calculate_progress function
def calculate_progress(tasks=task):
    completed = 0
    for task in tasks:
        if task['completed'] == True:
            completed += 1
    progress = completed / len(tasks) * 100
    return progress