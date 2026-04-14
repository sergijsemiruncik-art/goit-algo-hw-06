from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        def __init__(self, name):
            super().__init__(name)
            self.name = name

class Phone(Field):
    def __init__(self, phone: str):
        super().__init__(phone)
        if not isinstance(phone, str) or len(phone) != 10 or not phone.isdigit():
            raise ValueError('Phone must be 10 digits')

class Record:
    def __init__(self, name, phone = None):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone) is not None:
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
            return True
        return False

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str):
        found = self.find_phone(phone)
        if found is not None:
            self.phones.remove(found)
            return True
        return False

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)


    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())

        # Створення нової адресної книги


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("1234567890")
book.add_record(jane_record)

# Виведення всіх записів у книзі

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")
