def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_args(args):
    if len(args) != 2 or not args[1].isdigit():
        return False
    return True


def add_contact(args, contacts):
    if not validate_args(args):
        return "Invalid args."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if not validate_args(args):
        return "Invalid number phone."
    name, phone = args
    if not name in contacts.keys():
        return f"Name: {name} not found!"
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid name."
    name = args[0]
    if not name in contacts:
        return f"Name: {name} not found!"
    return contacts[name]


def show_all(contacts):
    formatted_list = []
    for name, phone in contacts.items():
        formatted_list.append(f"{name}: {phone}")

    return formatted_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit", "bye"]:
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
