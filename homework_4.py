import re

# Создаем пустой словарь для хранения контактов
phonebook = {}


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


# Собственное исключение для неверного формата номера телефона
class InvalidPhoneNumberError(Exception):
    pass


# Функция для проверки формата номера телефона
def validate_phone(phone):
    pattern = r"^\+380\(\d{2}\)\d{3}-(?:\d-\d{3}|\d{2}-\d{2})$"
    if not re.match(pattern, phone):
        raise InvalidPhoneNumberError()


# Функция-обработчик для команды "add"
@input_error
def add_contact(name, phone):
    try:
        validate_phone(phone)
        phonebook[name] = phone
        return f"Контакт {name} с номером телефона {phone} добавлен."
    except InvalidPhoneNumberError:
        raise ValueError()


# Функция-обработчик для команды "change"
@input_error
def change_contact(name, phone):
    if name in phonebook:
        try:
            validate_phone(phone)
            phonebook[name] = phone
            return f"Номер телефона для {name} обновлен."
        except InvalidPhoneNumberError:
            raise ValueError()
    else:
        return f"Контакт {name} не найден."


# Главная функция, в которой происходит взаимодействие с пользователем
def main():
    print("Бот-ассистент. Введите 'good bye', 'close' или 'exit' для выхода.")

    while True:
        user_input = input("Введите команду: ").strip().lower()

        if user_input in ("good bye", "close", "exit"):
            print("До свидания!")
            break
        else:
            handler = None
            if user_input == "hello":
                handler = hello
            elif user_input.startswith("add "):
                _, contact_info = user_input.split(" ", 1)
                try:
                    name, phone = contact_info.split()
                    handler = add_contact(name, phone)
                except ValueError:
                    print("Укажите имя и номер телефона, пожалуйста")
            elif user_input.startswith("change "):
                _, contact_info = user_input.split(" ", 1)
                try:
                    name, phone = contact_info.split()
                    handler = change_contact(name, phone)
                except ValueError:
                    print("Укажите имя и номер телефона, пожалуйста")
            elif user_input.startswith("phone "):
                _, name = user_input.split(" ", 1)
                handler = find_phone(name)
            elif user_input == "show all":
                handler = show_all

            if handler is not None:
                result = handler()
                if result:
                    print(result)
                else:
                    print(
                        "Неверная команда. Введите 'good bye', 'close', 'exit', 'hello' или 'add ...' для взаимодействия с ботом."
                    )


if __name__ == "__main__":
    main()
