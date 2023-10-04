phonebook = {}


def add_contact():
    name = input("Введіть ім'я контакту: ")
    phone = input("Введіть номер телефону: ")
    phonebook[name] = phone
    print(f"Контакт {name} з номером {phone} додано до телефонної книги.")


def find_contact():
    name = input("Введіть ім'я контакту, щоб знайти номер телефону: ")
    if name in phonebook:
        phone = phonebook[name]
        print(f"Номер телефону {name}: {phone}")
    else:
        print(f"Контакт з іменем {name} не знайдено.")


def update_contact():
    name = input("Введіть ім'я контакту, якого ви хочете оновити: ")
    if name in phonebook:
        new_phone = input(f"Введіть новий номер телефону для {name}: ")
        phonebook[name] = new_phone
        print(f"Номер телефону для {name} оновлено.")
    else:
        print(f"Контакт з іменем {name} не знайдено.")


def list_contacts():
    print("Список контактів:")
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")


while True:
    print("\nМеню:")
    print("1. Додати контакт")
    print("2. Знайти номер телефону")
    print("3. Оновити контакт")
    print("4. Вивести список контактів")
    print("5. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        list_contacts()
    elif choice == "5":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Оберіть опцію з меню.")
