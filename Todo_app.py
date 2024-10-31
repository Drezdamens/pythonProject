import functions
import time
import FreeSimpleGUI as sg
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")
clock = sg.Text(time.strftime("%b %d %Y, %H:%M:%S"), key="clock")
label = sg.Text("Write to-dos")
input_box = sg.InputText(tooltip="Enter the to-do", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do app",
                   layout=[[clock],
                           [label],[input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 10))
while True:
    event, values = window.read(timeout=1000)
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    window["clock"].update(value=time.strftime("%b %d %Y, %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            if not values["todo"].strip():
                sg.popup("Input the text", font=("Helvetica", 10))
            else:
                todos = functions.get_todos()
                new_todo = values["todo"] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)

                window["todos"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Pick an item first")
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Pick an item first", font=("Helvetica", 10))
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()