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

    return wrapper


# Функция-обработчик для команды "hello"
@input_error
def hello():
    return "Как я могу вам помочь?"


# Функция-обработчик для команды "add"
@input_error
def add_contact(name, phone):
    # Добавляем контакт в телефонную книгу
    phonebook[name] = phone
    return f"Контакт {name} с номером телефона {phone} добавлен."


# Функция-обработчик для команды "change"
@input_error
def change_contact(name, phone):
    if name in phonebook:
        # Обновляем номер телефона существующего контакта
        phonebook[name] = phone
        return f"Номер телефона для {name} обновлен."
    else:
        return f"Контакт {name} не найден."


# Функция-обработчик для команды "phone"
@input_error
def find_phone(name):
    if name in phonebook:
        # Находим номер телефона для указанного контакта
        return f"Номер телефона для {name}: {phonebook[name]}"
    else:
        return f"Контакт {name} не найден."


# Функция-обработчик для команды "show all"
@input_error
def show_all():
    if phonebook:
        # Выводим список всех контактов
        result = "Контакты:\n"
        for name, phone in phonebook.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "Телефонная книга пуста."


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
                handler = handle_command("hello")(hello)
            elif user_input.startswith("add "):
                _, contact_info = user_input.split(" ", 1)
                try:
                    name, phone = contact_info.split()
                    handler = handle_command("add")(add_contact)
                except ValueError:
                    print("Укажите имя и номер телефона, пожалуйста")
            elif user_input.startswith("change "):
                _, contact_info = user_input.split(" ", 1)
                try:
                    name, phone = contact_info.split()
                    handler = handle_command("change")(change_contact)
                except ValueError:
                    print("Укажите имя и номер телефона, пожалуйста")
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
                        "Неверная команда. Введите 'good bye', 'close', 'exit', 'hello' или 'add ...' для взаимодействия с ботом."
                    )


if __name__ == "__main__":
    main()
