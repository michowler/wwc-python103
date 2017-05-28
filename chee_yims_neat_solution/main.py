def create(todolists, name):
    todoitem = str(input("Enter your to-do item to add:"))
    todolist = todolists.get(name)
    todolist.append(todoitem)

def delete(todolists, name):
    todoitem = str(input("Enter your to-do item to remove:"))
    todolist = todolists.get(name)
    todolist.remove(todoitem)

def display(todolist):
    for k, v, in todolists.items():
        print("\n%s\'s to-do list is:" % k)
        for item in v:
            print("%s" % item)

def menu(name, todolists):
    message = """Options:
            1 - View your to-do lists
            2 - Create a to-do
            3 - Complete a to-do
            4 - Delete a to-do
            0 - Quit
            """
    while True:
        option = int(input(message))
        if option == 1:
            display(todolists)
        elif option == 2:
            create(todolists, name)
        elif option == 3:
            print("Complete a to-do")
        elif option == 4:
            print("Delete a to-do")
        elif option == 0:
            print("Quit, Bye Bye %s" % name)
            break
        else:
            print("Invalid input. Should be 0 - 4")

name = input('What is your name?')
print('Hello %s!' % name)
todolists = { name: [] }
#todolists = { "chee yim": ["learn python", "read something", "feed the dog"],
#              "lidya" : ["mentor python 102", "nasa hackathon"]
#            }
menu(name, todolists)
