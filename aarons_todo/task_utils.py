def save_to_file(todo_dict):
    filename = input('Please enter a filename')
    with open(filename, 'w') as file:
        file.write('Your TODOs\n')
        file.write('-'*50)
        file.write('\n\n')
        file.write('\n'.join(format_tasks(todo_dict)))

def format_tasks(todo_dict):
    formated_tasks = []
    for category in todo_dict:
        for task in todo_dict.get(category, []):
            formated_tasks.append('{}: {}'.format(category.capitalize(), task))
    return formated_tasks
