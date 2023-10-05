import re

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


phonebook = {}


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
        elif user_input == "hello":
            print(hello())
        elif user_input.startswith("add "):
            _, contact_info = user_input.split(" ", 1)
            try:
                name, phone = contact_info.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Give me name and phone please")
        elif user_input.startswith("change "):
            _, contact_info = user_input.split(" ", 1)
            try:
                name, phone = contact_info.split()
                print(change_contact(name, phone))
            except ValueError:
                print("Give me name and phone please")
        elif user_input.startswith("phone "):
            _, name = user_input.split(" ", 1)
            print(find_phone(name))
        elif user_input == "show all":
            print(show_all())
        else:
            print(
                "Invalid command. Type 'good bye', 'close', 'exit', 'hello', or 'add ...' to interact with the bot."
            )
            @input_error
def add_contact(name, phone):
    # Проверка формата номера и отсутствия лишних символов
    if re.match(r'^\+380\(\d\d\)\d{3}\-(\d\-\d{3}|\d{2}\-\d{2})$', phone):
        phonebook[name] = phone
        return f"Contact {name} with phone number {phone} added."
    else:
        return "Invalid phone number format or contains invalid characters. Please use the format +380(xx)xxx-xx-xx or +380(xx)xxx-xxx."

@input_error
def change_contact(name, phone):
    if name in phonebook:
        # Проверка формата номера и отсутствия лишних символов
        if re.match(r'^\+380\(\d\d\)\d{3}\-(\d\-\d{3}|\d{2}\-\d{2})$', phone):
            phonebook[name] = phone
            return f"Phone number for {name} updated."
        else:
            return "Invalid phone number format or contains invalid characters. Please use the format +380(xx)xxx-xx-xx or +380(xx)xxx-xxx."
    else:
        return f"Contact {name} not found."


if __name__ == "__main__":
    main()
