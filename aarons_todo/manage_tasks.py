def manage_tasks(todo_dict):
    while True:
        USER_ACTION_PROMPT = 'Either select a category, or type "exit" to return to the previous menu.'
        category = input(USER_ACTION_PROMPT + '\n' + get_categories(todo_dict))
        if category == 'exit': break
        manage_category(todo_dict, category)

def manage_category(todo_dict, category):
    USER_ACTION_PROMPT = '''Press (1) to view all tasks
Press (2) to mark a task complete
Press (3) to delete a task
Press (4) to exit to the previous menu
'''
    tasks = todo_dict[category]
    while True:
        user_action = input(USER_ACTION_PROMPT)
        if user_action == '1':
            print(print_all_tasks(tasks))
        elif user_action == '2':
            task_id = input('Enter a task number to complete task')
            complete_task(tasks, task_id)
        elif user_action == '3':
            delete_task(tasks, task_id)
        elif user_action == '4':
            break
        else:
            print('Invalid input, please select again.')

def print_all_tasks(tasks):
    tasks = format_tasks(tasks)
    return '\n'.join(tasks)

def complete_task(tasks, task_id):
    task = tasks[int(task_id)]
    task.complete_task()

def delete_task(tasks, task_id):
    del(tasks[int(task_id)])

def format_tasks(tasks):
    tasks = zip(range(len(tasks)), tasks)
    formated_tasks = []
    for task in tasks:
        formated_tasks.append('{}: {}'.format(task[0], task[1]))
    return formated_tasks

def get_categories(todo_dict):
    return '\n'.join(todo_dict.keys())
