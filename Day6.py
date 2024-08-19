# def print_shape(rows, columns):
#     for i in range(rows):
#         if i == 0 or i == rows - 1:
#             print('*' * columns)
#         else:
#             print('*' + ' ' * (columns - 2) + '*')
# rows = input("tedad satr ra vared konid: ")
# rows = int(rows)
# columns =input("tedad setun ra vared konid: ")
# columns = int(columns)
# print_shape(rows, columns)


user_prompt="Enter a todo: "
todos =[]

while True:
    user_action = input("Type add,edit, complete, show or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] +"\n"

        with open("../pythonProject/todos.txt", "r") as file:
            todos = file.readlines()


        todos.append(todo)

        with open("../pythonProject/todos.txt", "w") as file:
             file.writelines(todos)
    elif user_action.startswith("edit"):


        number=int(user_action[5:])
        with open("../pythonProject/todos.txt", "r") as file:
            todos = file.readlines()
        todos[number-1] = input("new todo: ")+"\n"
        with open("../pythonProject/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):

        with open("../pythonProject/todos.txt", "r") as file:
            todos = file.readlines()

        for index,todo in enumerate(todos):
            todo = todo.strip("\n")
            print(f"{index+1} - {todo}")

    elif user_action.startswith("complete"):
        with open("../pythonProject/todos.txt", "r") as file:
            todos = file.readlines()


        number = int(user_action[9:]) - 1
        todo_to_remove=todos[int(number)-1].strip("\n")
        todos.pop(number)
        with open("../pythonProject/todos.txt", "w") as file:
            file.writelines(todos)

        massage = f"todo {todo_to_remove} has been complete."
        print(massage)

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid input")

print("Done!")


