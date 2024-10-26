import functions
import FreeSimpleGUI as sg


label = sg.Text("Write to-dos")
input_box = sg.InputText(tooltip="Enter the to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-do app", layout=[[label],[input_box, add_button]])
window.read()
window.close()