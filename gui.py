import functions
import PySimpleGUI as sg

label = sg.Text("Enter Todo")
input_box = sg.InputText(key='todo')
btn_add = sg.Button("Add")
btn_edit = sg.Button("Edit")
btn_complete = sg.Button("Complete")
btn_exit = sg.Button("Exit")

layout = [
    [label, input_box, btn_add],
    [[btn_complete], btn_edit],
    [btn_exit]

]

window = sg.Window("TODO", layout, font=('Roboto', 20))

while True:
    event, values = window.read()
    # print(event)
    # print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)

        case sg.WINDOW_CLOSED:
            break

window.close()
