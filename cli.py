import functions
import time


now = time.strftime('%B %d , %Y - %H: %M : %S')
print(f"It is {now}")

while True:
    # Get user input and strip space , chars from it.
    user_choice = input("Type add, show,edit,complete or exit: ").lower()
    user_choice = user_choice.strip()

    if user_choice.startswith('add'):
        todo = user_choice[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo)
        functions.set_todos(todos)

    elif user_choice.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}.{item.capitalize()}")

    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])
            number -= 1
            todos = functions.get_todos()
            todos.pop(number)
            functions.set_todos(todos)

        except (IndexError, ValueError) as e:
            print("There's no item with that number")
            continue

    elif user_choice.startswith('edit'):
        try:
            number = int(user_choice[5:])
            number -= 1
            new_todo = input("Enter new todo: ")
            todos = functions.get_todos()
            todos[number] = new_todo + "\n"
            functions.set_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_choice.startswith("quit") or user_choice.startswith("exit"):
        break
    else:
        print('⚠️Command is not valid!\n')