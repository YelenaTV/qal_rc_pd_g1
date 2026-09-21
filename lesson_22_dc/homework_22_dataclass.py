# Завдання 1. Охоронці воріт
passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]

def is_strong(password):
    # Перевіряємо довжину пароля:
    # від 8 до 20 символів включно.
    correct_length = 8 <= len(password) <= 20

    # чи містить пароль хоча б одну цифру.
    has_digit = any(
        character.isdigit()
        for character in password
    )

    # чи містить пароль хоча б одну велику літеру.
    has_upper = any(
        character.isupper()
        for character in password
    )

    #  чи немає пробілу в паролі.
    no_spaces = " " not in password

    # Пароль надійний - всі чотири умови виконуються.
    return (
        correct_length
        and has_digit
        and has_upper
        and no_spaces
    )
strong_passwords = list(filter(lambda password: is_strong(password),passwords))
# Відбираємо паролі, які НЕ є надійними.
weak_passwords = list(filter(lambda password: not is_strong(password),passwords))
print("Надійні паролі:")

# Виводимо кожен надійний пароль.
for password in strong_passwords:
    print(f"✅ {password} — надійний")


print("\nНенадійні паролі:")

# Виводимо кожен ненадійний пароль.
for password in weak_passwords:
    print(f"❌ {password} — відхилено")

passwords = [
    "Cossack1",
    "sich",
    "ZAPORIZHZHIA2024",
    "Sich Gate 5",
    "Mazepa99",
    "короткий1",
    "BohunTheBrave",
    "D0br0nich!",
    "аааааааА1",
    "Valid1Pass",
]

### Завдання 2. Перепис козацького реєстру
from functools import reduce

raw_registry = [
    "  іван сірко  | полковник | 150",
    "БОГДАН ХМЕЛЬНИЦЬКИЙ | гетьман | 10000",
    "петро дорошенко|сотник|75",
    "  Іван Мазепа | гетьман | 30000 ",
    "семен палій  |  полковник  | 500",
    "  Григорій Сковорода | філософ | 0",
]
def parse_registry_row(row):
    # Розділяємо рядок за символом "|".
    parts = row.split("|")
    # Очищаємо пробіли навколо імені.
    name = parts[0].strip().title()
    # Очищаємо пробіли навколо посади
    # та робимо першу літеру великою.
    rank = parts[1].strip().capitalize()
    # Очищаємо пробіли та перетворюємо число з рядка в int.
    warriors = int(parts[2].strip())
    return {
        "name": name,
        "rank": rank,
        "warriors": warriors,
    }

registry = list(map(parse_registry_row, raw_registry))
active_registry = list(filter(lambda person: person["warriors"] > 0,registry))

total_warriors = reduce(lambda total, person: total + person["warriors"],active_registry,0)

sorted_registry = sorted(active_registry,key=lambda person: person["warriors"],reverse=True)

print("\nКозацький реєстр")
print(f"Кількість записів: {len(sorted_registry)}")
print("-" * 60)
print(f"{'№':<4}{'Ім’я':<25}{'Посада':<15}{'Воїни':>10}")
print("-" * 60)
# Виводимо записи у вигляді таблиці.
for number, person in enumerate(sorted_registry, start=1):
    print(
        f"{number:<4}"
        f"{person['name']:<25}"
        f"{person['rank']:<15}"
        f"{person['warriors']:>10}"
    )


print("-" * 60)
print(f"Разом воїнів: {total_warriors}")

### Завдання 3. Пошук козацьких шифрів

messages = [
    "А роза упала на лапу азора",
    "Козак",
    "Зараз",
    "level",
    "Python",
    "А баба",
    "racecar",
    "Запоріжжя",
    "noon",
    "Мазепа",
]
def is_palindrome(text):
    lower_text = text.lower()  #всі літери в нижній регістр.
    
    clean_text = lower_text.replace(" ", "") # Видаляємо пробіли.

    return clean_text == clean_text[::-1]

#  залишаємо лише паліндроми.
secret_messages = list(filter(lambda message: is_palindrome(message),messages))

def format_secret_message(message):
    
    clean_message = message.lower().replace(" ", "")# нижній регістр і видалити пробіли.

  
    return f"🔐 {message} → {clean_message[::-1]}"  # повідомлення у потрібному форматі.

formatted_messages = list(map(format_secret_message,secret_messages))

print("\nКозацькі шифри:")


for message in formatted_messages:
    print(message) #  всі знайдені паліндроми.