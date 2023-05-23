import PySimpleGUI as PSG

label1 = PSG.Text("Select file(s) to compress")
input1 = PSG.Input()
choose_button1 = PSG.FilesBrowse("Choose")

label2 = PSG.Text("Select destination to save")
input2 = PSG.Input()
choose_button2 = PSG.FolderBrowse("Choose")

compress_button = PSG.Button("Compress")

window = PSG.Window("File COmpressor", 
                    layout=[[label1, input1, choose_button1], 
                            [label2, input2, choose_button2],
                            [compress_button]])

window.read()
window.close()