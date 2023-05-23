import functions
import PySimpleGUI

label = PySimpleGUI.Text("type in a shopping list")
input_box = PySimpleGUI.InputText(tooltip="enter shopping list")
add_button = PySimpleGUI.Button("Add")


window = PySimpleGUI.Window('My app', layout=[[label, input_box, add_button]])
window.read()
window.close()