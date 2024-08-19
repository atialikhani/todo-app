FAILEPASTH ="todos.txt"
# constants
def get_todos(filename= FAILEPASTH):
    """
    get_todos returns a list of all todo items in a file and the file is received from argument
    :param filename: file morede nazar
    :return: list of todo items
    """
    with open(filename, 'r') as f:
        todos = f.readlines()
    return todos

def set_todos(todos, filename= FAILEPASTH):
    """
    set_todos get new todos list and then save in target file
    :param todos: list of todos
    :param filename: target file to write todos list
    """

    with open(filename, 'w') as f:
        f.writelines(todos)








# 14 تمرین
# def count(phrase):
#     return phrase.count('.')
