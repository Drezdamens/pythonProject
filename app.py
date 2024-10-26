import functions
import time

now = time.strftime("%b %Y, %H:%M:%S")
print("hello")
print("It is",now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            number = number - 1

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("You should input the number, not string")
            continue

    elif user_action.startswith("complete"):
        try:
            complete = int(user_action[9:])

            todos = functions.get_todos()
            
            deleted_todo = todos[complete - 1].strip("\n")
            todos.pop(complete - 1)

            functions.write_todos(todos)

            message = f"The action {deleted_todo} was completed"
            print(message)
        except IndexError:
            print("Your number is out of the list")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

print("Bye")

