def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Вкажи імʼя та номер телефону."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Вкажи імʼя та новий номер телефону."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Вкажи імʼя"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."

def show_all(contacts):
    if not contacts:
        return "Контакт не знайдено."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue  # Пропуск порожнього вводу

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
