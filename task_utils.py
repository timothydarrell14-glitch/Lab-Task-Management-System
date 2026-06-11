from datetime import datetime

# Import validation functions
from validation import validate_due_date
from validation import validate_task_description
from validation import validate_task_title

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    tasks.append({
        'title': title,
        'description': description,
        'due_date': due_date,
        'completed': False
    })
    
    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    task = tasks[index]
    task['completed'] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks = tasks):
    for task in tasks:
        if task['completed'] == False:
            print(task)

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    completed = 0
    for task in tasks:
        if task['completed'] == True:
            completed += 1
    progress = completed / len(tasks) * 100
    return progress