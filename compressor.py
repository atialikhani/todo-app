import PySimpleGUI as sg

label1 = sg.Text('select files to compress:')
input1 = sg.Input()
Choose_button1 = sg.FileBrowse('Choose')

label2 = sg.Text('select destination folder:')
input2 = sg.Input()
Choose_button2 = sg.FolderBrowse('Choose')

Compress_button = sg.Button('Compressor')

Window = sg.Window("File Compressor",
                   layout=[[label1, input1, Choose_button1],
                            [label2, input2, Choose_button2],
                            [Compress_button]])

Window.read()
Window.close()
