import functions
import PySimpleGUI as sg

label = sg.Text("Enter Todo")
input_box = sg.InputText()
btn_add = sg.Button("Add")
btn_edit = sg.Button("Edit")
btn_complete = sg.Button("Complete")
btn_exit = sg.Button("Exit")

layout = [
    [label, input_box, btn_add],
    [btn_edit, [btn_complete]],
    [btn_exit]

]

window = sg.Window("TODO", layout)

window.read()
window.close()
