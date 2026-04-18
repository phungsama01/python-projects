todos = []
while true:
    print("1. Add todo")
    print("2. View todos")
    print("3. Quit")
    choice = input("Choose: ")
    if choice == "1":
        todos = input("Enter todo list: ")
        todos.append(todo)
        print("Todo added")
    elif choice == "2":
        for todo in todos:
            print(todo)
    elif choice == "3":
        break