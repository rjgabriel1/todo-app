import functions
import PySimpleGUI as sg

label = sg.Text("Enter Todo")
input_box = sg.InputText(key='todo')
btn_add = sg.Button("Add")
btn_edit = sg.Button("Edit")
btn_complete = sg.Button("Complete")
btn_exit = sg.Button("Exit")
list_box = sg.Listbox(values=functions.get_todos(), key="items",
                      enable_events=True, size=(45, 10))
layout = [
    [label, input_box, btn_add],
    [list_box, btn_complete, btn_edit],
    [btn_exit]

]

window = sg.Window("TODO", layout, font=('Roboto', 20))

while True:
    event, values = window.read()


    match event:

        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window['items'].update(values=todos)

        case "Edit":
            todo_to_edit = values['items'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.set_todos(todos)
            window['items'].update(values=todos)

        case 'items':
            window['todo'].update(value=values['items'][0])

        case "Complete":
            completed_todo = values['items'][0]
            todos = functions.get_todos()
            index = todos.index(completed_todo)
            todos.pop(index)
            functions.set_todos(todos)
            window['items'].update(values=todos)

        case sg.WINDOW_CLOSED:
            break
        case "Exit":
            break
window.close()
