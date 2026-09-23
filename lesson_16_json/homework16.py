# Завдання 1. Перші кроки — серіалізація вручну
import json
single_record = {
    "title": "Ой у лузі червона калина",
    "genre": "пісня",
    "region": "Полтавщина",
    "narrator": "Ганна Остапенко",
    "year": 1932,
    "content": "Патріотична народна пісня.",
    "tags": ["патріотична", "народна", "історична"],
    "verified": True
}
# 1. Перетворення словника на JSON-рядок
json_string = json.dumps(single_record)

print("JSON-рядок без форматування:")
print(json_string)
print("Тип:", type(json_string))

# 2. Форматований JSON-рядок
pretty_json_string = json.dumps(
    single_record,
    indent=4,
    ensure_ascii=False
)

print("\nJSON-рядок із indent=4 та ensure_ascii=False:")
print(pretty_json_string)

print("\nПорівняння:")
print("- Без indent JSON записаний в один рядок.")
print("- indent=4 додає відступи, стає читабельним.")
print("- ensure_ascii=False  без кодів типу \\u041e.")

restored_record = json.loads(pretty_json_string)

print("\nВідновлений об'єкт:")
print(restored_record)
print("Тип:", type(restored_record))

print("Назва:", restored_record["title"])
print("Жанр:", restored_record["genre"])
print("Оповідач:", restored_record["narrator"])

# Завдання 2. Архів експедиції — запис і читання файлу
#Створи список із щонайменше **5 фольклорних записів** різних жанрів і регіонів.
archive_records = [
    {
        "title": "Ой у лузі червона калина",
        "genre": "пісня",
        "region": "Полтавщина",
        "narrator": "Ганна Остапенко",
        "year": 1932,
        "content": "Патріотична народна пісня.",
        "tags": ["патріотична", "народна"],
        "verified": True
    },
    {
        "title": "Про лисицю та журавля",
        "genre": "казка",
        "region": "Поділля",
        "narrator": "Марія Коваль",
        "year": 1954,
        "content": "Казка про гостювання лисиці та журавля.",
        "tags": ["тварини", "мораль"],
        "verified": True
    },
    {
        "title": "Легенда про Довбуша",
        "genre": "легенда",
        "region": "Карпати",
        "narrator": "Іван Бойко",
        "year": 1968,
        "content": "Легенда про відважного опришка.",
        "tags": ["героїчна", "історична"],
        "verified": False
    },
    {
        "title": "Без труда нема плода",
        "genre": "прислів'я",
        "region": "Слобожанщина",
        "narrator": "Петро Мельник",
        "year": 1975,
        "content": "Прислів'я про важливість праці.",
        "tags": ["праця", "мудрість"],
        "verified": True
    },
    {
        "title": "Ніч перед Івана Купала",
        "genre": "пісня",
        "region": "Полісся",
        "narrator": "Олена Ткаченко",
        "year": 1981,
        "content": "Обрядова пісня про свято Івана Купала.",
        "tags": ["обрядова", "літня"],
        "verified": True
    }
]

# 1)Запис/збереження списку у файл
with open("folklore_archive.json", "w", encoding="utf-8") as file:
    json.dump(
        archive_records,
        file,
        indent=4,
        ensure_ascii=False
    )

# 2)Читання файлу
with open("folklore_archive.json", "r", encoding="utf-8") as file:
    loaded_archive = json.load(file)


print("\nЗавдання 2:")
#і переконайся, що кількість записів збереглась.
print("Кількість записів до збереження:", len(archive_records))
print("Кількість записів після завантаження:", len(loaded_archive))
#3)Виведення заголовків
print("\nЗаголовки записів:")
for number, record in enumerate(loaded_archive, start=1):
    print(
        f'{number}. "{record["title"]}" '
        f'({record["genre"]}, {record["region"]})'
    )

# Завдання 3. Клас FolkloreRecord


class FolkloreRecord:
    def __init__(
        self,
        title,
        genre,
        region,
        narrator,
        year,
        content,
        tags,
        verified
    ):
        self.title = title
        self.genre = genre
        self.region = region
        self.narrator = narrator
        self.year = year
        self.content = content
        self.tags = tags
        self.verified = verified
#повертає словник із усіма атрибутами
    def to_dict(self):
        return {
            "title": self.title,
            "genre": self.genre,
            "region": self.region,
            "narrator": self.narrator,
            "year": self.year,
            "content": self.content,
            "tags": self.tags,
            "verified": self.verified
        }

    @classmethod
    #класовий метод, що створює об'єкт зі словника
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            genre=data["genre"],
            region=data["region"],
            narrator=data["narrator"],
            year=data["year"],
            content=data["content"],
            tags=data["tags"],
            verified=data["verified"]
        )
#повертає:
#```
#[пісня] "Ой у лузі червона калина" — Полтавщина, 1932 (оповідач: Ганна Остапенко)
#```
    def __str__(self):
        return (
            f'[{self.genre}] "{self.title}" — '
            f'{self.region}, {self.year} '
            f'(оповідач: {self.narrator})'
        )

#Створи 3 об'єкти `FolkloreRecord`
record_1 = FolkloreRecord(
    "Ой у лузі червона калина",
    "пісня",
    "Полтавщина",
    "Ганна Остапенко",
    1932,
    "Патріотична народна пісня.",
    ["патріотична", "народна"],
    True
)

record_2 = FolkloreRecord(
    "Про лисицю та журавля",
    "казка",
    "Поділля",
    "Марія Коваль",
    1954,
    "Казка про гостювання лисиці та журавля.",
    ["тварини", "мораль"],
    True
)

record_3 = FolkloreRecord(
    "Легенда про Довбуша",
    "легенда",
    "Карпати",
    "Іван Бойко",
    1968,
    "Легенда про відважного опришка.",
    ["героїчна", "історична"],
    False
)

records = [record_1, record_2, record_3]


# Збереження об'єктів
with open("records.json", "w", encoding="utf-8") as file:
    json.dump(
        [record.to_dict() for record in records],
        file,
        indent=4,
        ensure_ascii=False
    )


# Завантаження та відновлення об'єктів
with open("records.json", "r", encoding="utf-8") as file:
    records_data = json.load(file)

restored_records = [
    FolkloreRecord.from_dict(data)
    for data in records_data
]


print("\nЗавдання 3:")
for record in restored_records:
    print(record)

# Завдання 4. Клас FieldExpedition
#польова експедиція збирача фольклору.
class FieldExpedition:
    
    def __init__(self, expedition_id, researcher, location, date):
        self.expedition_id = expedition_id #унікальний номер
        self.researcher = researcher    #ім'я дослідника
        self.location = location #село або місто
        self.date = date  #дата у форматі рядка `"РРРР-ММ-ДД"`
        self.records = [] #список об'єктів `FolkloreRecord`, початково порожній

    def add_record(self, record):   #додає об'єкт `FolkloreRecord` до списку. Якщо запис із таким `title` вже є — повертає `"Запис '<title>' вже є в експедиції"`
        for existing_record in self.records:
            if existing_record.title == record.title:
                return f"Запис '{record.title}' вже є в експедиції"

        self.records.append(record)
        return f"Запис '{record.title}' додано"

    def remove_record(self, title):  #видаляє запис за назвою. Якщо не знайдено — повертає `"Запис '<title>' не знайдено"`
        for record in self.records:
            if record.title == title:
                self.records.remove(record)
                return f"Запис '{title}' видалено"

        return f"Запис '{title}' не знайдено"

    def find_by_genre(self, genre): #повертає список усіх записів заданого жанру. Якщо нічого немає — порожній список

        return [
            record
            for record in self.records
            if record.genre == genre
        ]

    def to_dict(self): #повертає словник, де `records` — це список словників через `to_dict()` кожного запису
        return {
            "expedition_id": self.expedition_id,
            "researcher": self.researcher,
            "location": self.location,
            "date": self.date,
            "records": [
                record.to_dict()
                for record in self.records
            ]
        }

    @classmethod
    def from_dict(cls, data): #класовий метод, що відновлює об'єкт разом із усіма вкладеними `FolkloreRecord`
        expedition = cls(
            expedition_id=data["expedition_id"],
            researcher=data["researcher"],
            location=data["location"],
            date=data["date"]
        )

        expedition.records = [
            FolkloreRecord.from_dict(record_data)
            for record_data in data["records"]
        ]

        return expedition

    def save(self, filepath): #зберігає експедицію у JSON-файл
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(
                self.to_dict(),
                file,
                indent=4,
                ensure_ascii=False
            )

    @classmethod
    def load(cls, filepath): #класовий метод, що завантажує експедицію з файлу. Обробляє `FileNotFoundError` та `json.JSONDecodeError`
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

            return cls.from_dict(data)

        except FileNotFoundError:
            print(f"Помилка: файл '{filepath}' не знайдено.")
            return None

        except json.JSONDecodeError:
            print(f"Помилка: файл '{filepath}' містить некоректний JSON.")
            return None


expedition = FieldExpedition(
    expedition_id="EXP-001",
    researcher="Олександр Шевченко",
    location="село Великі Сорочинці",
    date="2026-09-23"
)

print("\nЗавдання 4:")

print(expedition.add_record(record_1))
print(expedition.add_record(record_2))
print(expedition.add_record(record_3))
#Створи експедицію, додай 4 записи різних жанрів(вище ще 3)
record_4 = FolkloreRecord(
    "Без труда нема плода",
    "прислів'я",
    "Слобожанщина",
    "Петро Мельник",
    1975,
    "Прислів'я про важливість праці.",
    ["праця", "мудрість"],
    True
)

print(expedition.add_record(record_4))

# Перевірка дубліката
print(expedition.add_record(record_1))

# Збереження експедиції
expedition.save("expedition.json")
print("Експедицію збережено у файл expedition.json")


# Завантаження в новий об'єкт
loaded_expedition = FieldExpedition.load("expedition.json")

if loaded_expedition is not None:
    print(
        "Експедицію завантажено:",
        loaded_expedition.expedition_id
    )
#Знайди всі пісні через `find_by_genre()`
    songs = loaded_expedition.find_by_genre("пісня")

    print("\nПісні в експедиції:")
    for song in songs:
        print(song)
#- Видали один запис і збережи знову
    print(
        loaded_expedition.remove_record("Легенда про Довбуша")
    )

    print(
        loaded_expedition.remove_record("Невідомий запис")
    )

    loaded_expedition.save("expedition_after_remove.json")
    print("Оновлену експедицію збережено.")

# Завдання 5. Центральний архів— робота з колекцією файлів


def merge_archives(filepaths):
    all_records = []
    #existing_titles = set()
    for filepath in filepaths:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)  #Завантажує всі записи з усіх файлів

            expedition = FieldExpedition.from_dict(data)
            all_records.extend(expedition.records)
            #for record in expedition.records:
             #   if record.title not in existing_titles:
              #      all_records.append(record)
               #     existing_titles.add(record.title)
        except FileNotFoundError:
            print(f"Попередження: файл '{filepath}' не знайдено.")

        except json.JSONDecodeError:
            print(
                f"Попередження: файл '{filepath}' "
                "містить пошкоджений JSON."
            )

        except KeyError as error:
            print(
                f"Попередження: у файлі '{filepath}' "
                f"відсутнє поле {error}."
            )

    return all_records #Повертає єдиний список усіх `FolkloreRecord` з усіх експедицій
#Якщо якийсь файл не існує або пошкоджений — пропускає його і виводить попередження


def filter_records(
    records,
    genre=None,
    region=None,
    verified=None
):
    filtered = []

    for record in records:
        if genre is not None and record.genre != genre:
            continue

        if region is not None and record.region != region:
            continue

        if verified is not None and record.verified != verified:
            continue

        filtered.append(record)

    return filtered  #Повертає лише ті записи, що відповідають усім переданим фільтрам
#Якщо жоден фільтр не передано — повертає всі записи

def export_summary(records, filepath):
    summary = [] #Приймає список `FolkloreRecord`

    for record in records: #Зберігає у JSON-файл не повні записи, а лише зведення:
        summary.append({
            "title": record.title,
            "genre": record.genre,
            "region": record.region,
            "verified": record.verified
        })

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            summary,
            file,
            indent=4,
            ensure_ascii=False
        )


# Створюємо ще одну експедицію
second_expedition = FieldExpedition(
    expedition_id="EXP-002",
    researcher="Наталія",
    location="місто Косів",
    date="2026-09-21"
)

second_expedition.add_record(record_3)
second_expedition.add_record(record_4)

second_expedition.save("expedition_2.json")


# Створюємо третю експедицію
third_expedition = FieldExpedition(
    expedition_id="EXP-003",
    researcher="Андрій",
    location="село Криворівня",
    date="2026-09-22"
)

third_expedition.add_record(record_1)
third_expedition.save("expedition_3.json")


print("\nЗавдання 5:")

archive_files = [
    "expedition.json",
    "expedition_2.json",
    "expedition_3.json",
    "missing_file.json"
]

merged_records = merge_archives(archive_files)

print("Загальна кількість об'єднаних записів:", len(merged_records))


filtered_records = filter_records( #Відфільтруй перевірені записи з певного регіону
    merged_records,
    region="Полтавщина",
    verified=True
)

print("\nПеревірені записи з Полтавщини:")
for record in filtered_records:
    print(record)

#Збережи зведення через `export_summary()`
export_summary(
    filtered_records,
    "summary.json"
)

print("\nЗведення збережено у файл summary.json")