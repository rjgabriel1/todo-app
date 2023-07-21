import functions
import PySimpleGUI as sg
import time

sg.theme('BlueMono')
clock = sg.Text('', key='clock')
label = sg.Text("Enter Todo")
input_box = sg.InputText(key='todo', tooltip="Enter Todo")
btn_add = sg.Button("Add", size=5)
btn_edit = sg.Button("Edit", size=5)
btn_complete = sg.Button("Complete", size=8)
btn_exit = sg.Button("Exit", size=5)
list_box = sg.Listbox(values=functions.get_todos(), key="items",
                      enable_events=True, size=(45, 10))
layout = [[clock],
          [label, input_box, btn_add],
          [list_box, btn_complete, btn_edit],
          [btn_exit]
          ]

window = sg.Window("TODO", layout, font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)

    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window['items'].update(values=todos)
            window['todo'].update(value='')

        case "Edit":
            try:
                todo_to_edit = values['items'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.set_todos(todos)
                window['items'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Edit task', 'Please select an item first', font=("Helvetica", 16))
        case 'items':
            window['todo'].update(value=values['items'][0])

        case "Complete":
            try:
                completed_todo = values['items'][0]
                todos = functions.get_todos()
                index = todos.index(completed_todo)
                todos.pop(index)
                functions.set_todos(todos)
                window['items'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Complete task', 'Please select an item first', font=("Helvetica", 16))

        case sg.WINDOW_CLOSED:
            break
        case "Exit":
            break
window.close()
