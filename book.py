books = []
while true:
    print("1. Add book")
    print("2. View books")
    print("3. Quit")
    choice = input("choose: ")
    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author: ")
        books.append({"name": wonder, "author": preetam})
        print("Book added!!")
    elif choice == "2":
        for book in books:
            print(name["wonder"] + " - " + author["preetam"])
    elif choice = "3":
        break

