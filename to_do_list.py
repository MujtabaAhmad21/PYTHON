import pyfiglet
ascii_banner = pyfiglet.figlet_format("TODOS")
print(ascii_banner)

# a user can add todos by entering them into the prompt
# a user can complete todos by entering the todos corresponding number
# a user can view a help screen by typing 'h' or 'help'
# a user can quit by typing 'quit' or 'q'

quitlist = ['q', 'quit', 'Q', 'QUIT']
helplist = ['h', 'help', 'H', 'HELP']
todo_list = []
completedlist = []
user_input = ""

while user_input not in quitlist:
    print("*" * 34)
    user_input = input("Enter a command. Type 'h' for help: \n> ")
    if user_input in quitlist:
        print(f"Today you completed {len(completedlist)} tasks:-")
        for task in completedlist:
            print(f"# {task}")
        break
    elif user_input in helplist:
        print("TODO LIST HELP")
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo, enter its number")
    elif user_input in "0123456789":
        if int(user_input) >= len(todo_list):
            print("There is no todo with that number.")
        else:
            completedlist.append(todo_list.pop(int(user_input)-1))
    else:
        todo_list.append(user_input)

    for index in range(len(todo_list)):
        print(f"{index+1}) {todo_list[index]}")