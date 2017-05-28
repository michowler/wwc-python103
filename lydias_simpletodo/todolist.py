# WWCode Kuala Lumpur Python 102 - Simple Todo List

from todoitem import *

def add(todo_list):
    # Adds an item to the list
    print("\nEnter your to-do:")
    text = input()

    if not todo_list:
        lastId = 0
    else:
        try:
            lastId = todo_list[-1].id
        except IndexError:
            # No items in list
            lastId = 0

    new_item = TodoItem(lastId + 1, text)
    todo_list.append(new_item)

    print("\n%s is added" % new_item.text)

def remove(todo_list):
    print("\nEnter a todo item Id:")
    item_id = int(input())

    # removes a todo item by id
    item = todo_list[item_id - 1]
    del todo_list[item_id - 1]
    print("\n%s is deleted" % item.text)

def mark_done(todo_list):
    print("\nEnter a todo item Id:")
    item_id = int(input())

    # mark a todo item as done
    item = todo_list[item_id - 1]
    item.done = True
    print("\n%s is done" % item.text)

def create(name):
    # creates a new todo object
    todo_book = {'Owner' : name, 'List': []}
    return todo_book

def display(todo_book):
    # prints the todo list
    print("\n%s's To-Do" % todo_book['Owner'])
    todo_list = todo_book['List']

    # check if todo list is empty
    if not todo_list:
        print("Your to-do list is empty.")
        return

    # print todo list
    for todo in todo_list:
        print (todo)

def menu(name):
    # prints the main menu
    print("\nHello %s!" % name)
    options = ("Options:\n"
               "1 - View your to-do lists\n"
               "2 - Create a to-do\n"
               "3 - Complete a to-do\n"
               "4 - Delete a to-do\n"
               "0 - Quit\n")
    choice = input(options)
    return int(choice)

def run():
    # The beginning...
    print("What is your name?")
    name = input()

    # The list
    todo_book = create(name)
    todo_list = todo_book['List']

    while True:
        choice = menu(todo_book['Owner'])

        if choice == 1:
            display(todo_book)
        elif choice == 2:
            add(todo_list)
        elif choice == 3:
            mark_done(todo_list)
        elif choice == 4:
            remove(todo_list)
        elif choice == 0:
            break

# Run the app
run()
