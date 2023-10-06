import re

# Создаем пустой словарь для хранения контактов
phonebook = {}


# Собственное исключение для неверного формата номера телефона
class InvalidPhoneNumberError(Exception):
    pass


# Функция для проверки формата номера телефона
def validate_phone(phone):
    pattern = r"^\+380\(\d{2}\)\d{3}-(?:\d-\d{3}|\d{2}-\d{2})$"
    if not re.match(pattern, phone):
        raise InvalidPhoneNumberError()


# Создаем декоратор input_error для обработки ошибок
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Введите имя пользователя"
        except ValueError:
            return "Укажите имя и номер телефона, пожалуйста"
        except IndexError:
            return "Неверный формат ввода. Формат: команда имя номер"
        except InvalidPhoneNumberError:
            return "Неверный формат номера телефона. Используйте формат +380(xx)xxx-xx-xx или +380(xx)xxx-xxx."

    return wrapper


# Функция-обработчик для команды "add"
@input_error
def add_contact(name, phone):
    validate_phone(phone)
    phonebook[name] = phone
    return f"Контакт {name} с номером телефона {phone} добавлен."


# Функция-обработчик для команды "change"
@input_error
def change_contact(name, phone):
    if name in phonebook:
        validate_phone(phone)
        phonebook[name] = phone
        return f"Номер телефона для {name} обновлен."
    else:
        return f"Контакт {name} не найден."


# Функция-обработчик для команды "hello"
@input_error
def hello():
    return "Как я могу вам помочь?"


# Функция-обработчик для команды "phone"
@input_error
def find_phone(name):
    if name in phonebook:
        return f"Номер телефона для {name}: {phonebook[name]}"
    else:
        return f"Контакт {name} не найден."


# Функция-обработчик для команды "show all"
@input_error
def show_all():
    if phonebook:
        result = "Контакты:\n"
        for name, phone in phonebook.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "Телефонная книга пуста."


# Функция для обработки команды "add"
def handle_add_command(contact_info):
    try:
        name, phone = contact_info.split()
        return add_contact(name, phone)
    except ValueError:
        return "Укажите имя и номер телефона, пожалуйста"


# Функция для обработки команды "change"
def handle_change_command(contact_info):
    try:
        name, phone = contact_info.split()
        return change_contact(name, phone)
    except ValueError:
        return "Укажите имя и номер телефона, пожалуйста"


# Функция для обработки команд пользователя
def handle_user_input(user_input):
    handlers = {
        "hello": hello,
        "add": handle_add_command,
        "change": handle_change_command,
        "phone": find_phone,
        "show all": show_all,
    }

    command_parts = user_input.split(" ", 1)
    command = command_parts[0]
    args = command_parts[1] if len(command_parts) > 1 else ""

    handler = handlers.get(command)
    if handler:
        return handler(args)
    else:
        return "Неверная команда. Введите 'good bye', 'close', 'exit', 'hello' или 'add ...' для взаимодействия с ботом."


# Главная функция, в которой происходит взаимодействие с пользователем
def main():
    print("Бот-ассистент. Введите 'good bye', 'close' или 'exit' для выхода.")

    while True:
        user_input = input("Введите команду: ").strip().lower()

        if user_input in ("good bye", "close", "exit"):
            print("До свидания!")
            break
        else:
            result = handle_user_input(user_input)
            print(result)


if __name__ == "__main__":
    main()
