from phone import Phone
from name import Name

class Record:
  # Представляє запис контакту, що містить ім'я та список номерів телефону.

  def __init__(self, name):
    # Ініціалізує запис з ім'ям та порожнім списком телефонів.
    self.name = Name(name)
    self.phones = []

  def __str__(self):
    # Повертає рядкове представлення запису.
    return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

  def add_phone(self, number: str):
    # Додає номер телефону до запису.
    self.phones.append(Phone(number))

  def remove_phone(self, number: str):
    # Видаляє номер телефону із запису.
    self.phones = list(filter(lambda phone: phone == number, self.phones))

  def edit_phone(self, old_number, new_number):
    # Редагує номер телефону у записі.
    self.phones = list(
      map(lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones)
    )

  def find_phone(self, number):
    # Знаходить номер телефону у записі.
    for phone in self.phones:
      if phone.value == number:
        return phone
