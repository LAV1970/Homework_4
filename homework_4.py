import re

phonebook = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input. Format: command name phone"

    return wrapper


def handle_command(command_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_input = input("Enter a command: ").strip().lower()

            if user_input == command_name:
                return func(*args, **kwargs)
            else:
                return None  # Возвращаем None, если команда не соответствует декорированной функции

        return wrapper

    return decorator


@input_error
def hello():
    return "How can I help you?"


@input_error
def add_contact(name, phone):
    phonebook[name] = phone
    return f"Contact {name} with phone number {phone} added."


@input_error
def change_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        return f"Phone number for {name} updated."
    else:
        return f"Contact {name} not found."


@input_error
def find_phone(name):
    if name in phonebook:
        return f"Phone number for {name}: {phonebook[name]}"
    else:
        return f"Contact {name} not found."


@input_error
def show_all():
    if phonebook:
        result = "Contacts:\n"
        for name, phone in phonebook.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "Phonebook is empty."


def main():
    print("Bot Assistant. Type 'good bye', 'close', or 'exit' to exit.")

    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input in ("good bye", "close", "exit"):
            print("Good bye!")
            break
        else:
            handler = None
            if user_input == "hello":
                handler = handle_command("hello")(hello)
            elif user_input.startswith("add "):
                _, contact_info = user_input.split(" ", 1)
                try:
                    name, phone = contact_info.split()
                    handler = handle_command("add")(add_contact)
                except ValueError:
                    print("Give me name and phone please")
            elif user_input.startswith("change "):
                _, contact_info = user_input.split(" ", 1)
                try:
                    name, phone = contact_info.split()
                    handler = handle_command("change")(change_contact)
                except ValueError:
                    print("Give me name and phone please")
            elif user_input.startswith("phone "):
                _, name = user_input.split(" ", 1)
                handler = handle_command("phone")(find_phone)
            elif user_input == "show all":
                handler = handle_command("show all")(show_all)

            if handler is not None:
                result = handler()
                if result:
                    print(result)
                else:
                    print(
                        "Invalid command. Type 'good bye', 'close', 'exit', 'hello', or 'add ...' to interact with the bot."
                    )


if __name__ == "__main__":
    main()
