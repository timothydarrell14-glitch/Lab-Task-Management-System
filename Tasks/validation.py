from datetime import datetime

def validate_task_title(title):
    if title != "":
        pass
    else:
        title = input("Please enter a Title")
    
def validate_task_description(description):
    if description != "":
        pass
    else:
        description = input("Please enter a description")
    
def validate_due_date(due_date):
    if datetime.strptime(due_date, "%Y-%m-%d"):
        pass
    else:
        due_date = input("Please enter a valid date in the format YYYY-MM-DD")