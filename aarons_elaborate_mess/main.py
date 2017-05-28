from .tasks import *
from .manage_tasks import *
from .task_utils import *

USER_ACTION_PROMPT = '''Press (1) to add a task
Press (2) to manage tasks
Press (3) to save tasks to a file
Press (4) to exit
'''

def run_program():
    todo_dict = {}
    while True:
        user_action = input(USER_ACTION_PROMPT)
        if user_action == '1':
            todo_dict = add_task(todo_dict)
        elif user_action == '2':
            manage_tasks(todo_dict)
        elif user_action == '3':
            save_to_file(todo_dict)
        elif user_action == '4':
            break
        else:
            print('Invalid input, please select again.')
