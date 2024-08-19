user_prompt="Enter a todo: "
todos =[]

while True:
    user_action = input("Type add,edit, show or exit: ")

    match user_action:
        case "edit":
            number =input("enter number of todo to edit: ")
            number=int(number)
            todos[number-1] = input("new todo: ")
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                 print(item.capitalize())
        case "exit":
            break
#
#

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
