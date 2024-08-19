# n = int(input("Enter a number: "))
#
# for i in range(0, n):
#     for j in range(0, n):
#         if (i == 0 or i == n-1 or j == 0 or j == n-1):
#             print("*", end="")
#         else:
#             print((i*j)[-1], end="")
#     print()

#
# import PySimpleGUI as sg
#
# label = sg.Text("What are dolphins?")
# option1 = sg.Radio("Amphibians", group_id="question1", key="Amphibians")
# option2 = sg.Radio("Fish", group_id="question1", key="Fish")
# option3 = sg.Radio("Mammals", group_id="question1", key="Mammals")
# option4 = sg.Radio("Birds", group_id="question1", key="Birds")
#
# window = sg.Window("File Compressor",
#                    layout=[[label],
#                            [option1],
#                            [option2],
#                             [option3],
#                             [option4],
#                            ])
#
# window.read()
# window.close()


while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = values["kms"]
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()
However, when the user runs the code above, enters a number, and presses the Convert button, the program stops, and an error is displayed in the command line:

TypeError: can't multiply sequence by non-int of type 'float'