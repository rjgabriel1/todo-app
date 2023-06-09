FILEPATH = "files/todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return a list of
    to-do items.
    """
    with open(filepath, "r") as file:
        todo_list = file.readlines()
    return todo_list


def set_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


