FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a txt. file and get a list of it."""
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list to a txt. file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)