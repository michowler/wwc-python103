from datetime import datetime

class Task(object):
    priority = 3

    def __init__(self, description):
        self.description = description
        self.complete = False
        self.created_date = datetime.now()
        self.completed_date = None

    def complete_task(self):
        self.completed_date = datetime.now()
        self.complete = True

    def is_task_complete(self):
        return self.complete == True

    def get_priority():
        return self.priority

    def __repr__(self):
        return '<< Low Priority Task: ' + self.description + ' >>'


class HighPriorityTask(Task):
    priority = 5

    def __repr__(self):
        return '<< HIGH PRIORITY TASK: {} >>'.format(self.description)

def add_task(todo_dict):
    category, task, priority = get_category_task_and_priority_from_user()
    todo_dict = create_category_if_not_present(todo_dict, category)
    task_object = build_task(task, priority=priority)
    todo_dict[category].append(task_object)
    return todo_dict

def get_category_task_and_priority_from_user():
    category = input('Enter a task category ')
    task = input('Enter a task ')
    priority = input('What is this tasks priority? (Enter "low" or "high") ')
    return category, task, priority

def create_category_if_not_present(todos, category):
    if category not in todos:
        todos.update({category: []})
    return todos

def build_task(task_description, priority='low'):
    if priority == 'low':
        return Task(task_description)
    else:
        return HighPriorityTask(task_description)
