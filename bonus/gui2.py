import PySimpleGUI as PSG

label1 = PSG.Text("Enter feet")
input1 = PSG.Input()
label2 = PSG.Text("Enter Inches")
input2 = PSG.Input()

convert = PSG.Button("Convert")

window = PSG.Window("Convertor", layout=[[label1, input1], [label2, input2], [convert]])

window.read()
window.close()