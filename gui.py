import functions
import PySimpleGUI

label = PySimpleGUI.Text("type in a shopping list")
input_box = PySimpleGUI.InputText(tooltip="enter shopping list", key='shopping item')
add_button = PySimpleGUI.Button("Add")


window = PySimpleGUI.Window('My shopping list app', 
                            layout=[[label, input_box, add_button]], 
                            font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.add_to_lists()
window.close()