FILEPATH = 'todos.txt'


def write_todos(todos_arg, filepath=FILEPATH):
    """writes todos in a textfile,
    default todos.txt"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def get_todos(filepath=FILEPATH):
    """read the todos from a textfile,
    default todos.txt"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
