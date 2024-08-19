#
# for i in range(1, 5):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

def print_shape(rows, columns):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print('*' * columns)
        else:
            print('*' + ' ' * (columns - 2) + '*')
rows = input("tedad satr ra vared konid: ")
rows = int(rows)
columns =input("tedad setun ra vared konid: ")
columns = int(columns)
print_shape(rows, columns)


# user_prompt="Enter a todo: "
# todos =[]
#
# while True:
#     user_action = input("Type add,edit, show or exit: ")
#
#     match user_action:
#         case "edit":
#             number =input("enter number of todo to edit: ")
#             number=int(number)
#             todos[number-1] = input("new todo: ")
#         case "add":
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case "show":
#             for index,todo in enumerate(todos):
#                 # print(index+1, "-", todo)
#                   print(f"{index+1} - {todo}")
#         case "complete":
#             number = input("enter number of todo to complete: ")
#             todos.pop(int(number) -1 )
#         case "exit":
#             break
#
# print("Done!")
#
#
