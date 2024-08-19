from modules.functions import get_todos, set_todos

import time

user_prompt ="Enter a todo:"
todos =[]

now = time.strftime("%a, %d %b %Y %H:%M:%S")
print("it is ", now)
while True:
    user_action = input("Type add,edit, complete, show or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] +"\n"

        todos =get_todos("todos.txt")

        todos.append(todo)

        set_todos(todos, "todos.txt")
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            todos =get_todos("todos.txt")
            todos[number-1] = input("new todo: ")+"\n"
            set_todos(todos, "todos.txt")
        except ValueError:
            print("Invalid input")
    elif user_action.startswith("show"):
        todos =get_todos("todos.txt")

        for index,todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1} - {todo}")

    elif user_action.startswith("complete"):
        try:

            todos =get_todos("todos.txt")
            number = int(user_action[9:]) - 1
            todo_to_remove=todos[int(number)-1].strip("\n")
            todos.pop(number)
            set_todos(todos, "todos.txt")
            massage = f"todo {todo_to_remove} has been complete."
            print(massage)
        except ValueError:
            print("todos not found(number out of range)")
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")

print("Done!")


