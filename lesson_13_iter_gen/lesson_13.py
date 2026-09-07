## Завдання 1: Ітератор «Ланцюжок доручень»
class ChainOfOrders:
    def __init__(self, name):
        self.name = name #  Зберігаємо список у змінну об’єкта
        self.index = 0  # Починаємо з першої людини в списку

    def __iter__(self): ## Метод, який робить об’єкт ітератором
        return self #Повертаємо сам об’єкт

    def __next__(self): # Метод, який повертає наступний рядок
        if self.index>=len(self.name): # Якщо індекс уже за межами списку
            raise StopIteration         # Зупиняємо ітерацію
        list_name = self.name[self.index]  # Беремо поточну людину зі списку

        if len(self.name) == 1: # Якщо в списку лише одна людина
            self.index = self.index+1    # Зсуваємо індекс вперед, щоб наступний виклик завершився
            return f"{list_name} каже: теля прив'язав!"

        if self.index == len(self.name) - 1:                # Якщо це остання людина в списку
            self.index = self.index + 1                     # Зсуваємо індекс вперед
            return f"{list_name} каже: теля прив'язав!"     # Останній учасник завершує ланцюжок

        next_name = self.name[self.index + 1]

        if next_name == "Дід":
            next_form = "Діду"
        elif next_name == "Батько":
            next_form = "Батькові"
        elif next_name == "Михайлик":
            next_form = "Михайлику"
        elif next_name == "Василько":
            next_form = "Василькові"
        else:
            next_form = next_name

        self.index = self.index + 1

        return f"{list_name} каже {next_form}: передай далі!"

chain = ChainOfOrders(["Дід", "Батько", "Михайлик", "Василько"])

for message in chain:
    print(message)

## Завдання 2: Генератор «Чутка по селу»
def village_rumor(start_message, people):
    if not people: # якщо список порожній, то нічого передавати, тому функція просто завершується
        return
    message = start_message # зберігаємо початкову чутку в окрему змінну

    for index, person in enumerate(people):  #проходимо по списку людей і одночасно маємо номер елемента
        if index == 0:  #перша людина просто говорить оригінальне повідомлення
            yield f'{person} каже: "{message}"' #повертаємо першу версію чутки
        else:
            message = message + f" (переказала {people[index -1]})" #Кожна наступна: людина «переказує по-своєму» — додає в кінець повідомлення `"(переказав <ім'я>)"`
            if index == len(people) - 1:
                message = message + " (і всі дізналися!)"  #остання людина додає фінальну фраз
            yield f'{person} переказує: "{message}"'

for version in village_rumor("Теля втекло!", ["Горпина", "Параска", "Явдоха", "Оксана"]):
    print(version)

## Завдання 3: Генераторний вираз «Скільки разів передали»
#count = 0

#for event in events:
 #   if "передав документи" in event:
   #     count = count + 1
events = [  # список усіх подій.
    "Михайлик передав доручення",
    "Василько відмовився",
    "Грицько передав доручення",
    "Оленка прив'язала теля",
    "Данилко передав доручення",
]
filter_events = (event for event in events if "передав доручення" in event) # генератор, який залишає тільки події з фразою "передав доручення
count = sum(1 for _ in filter_events)  #рахує, скільки таких подій є
print(f"Доручення передавали {count} рази")

## Завдання 4: Нескінченний генератор «Черга на толоці»
import itertools

def toloka_queue(workers):
    while True:
        for worker in workers:
            yield f" Черга: {worker}"
queue = toloka_queue(["Іван", "Марія", "Степан"])

# Взяти перші 7 чергувань
for turn in itertools.islice(queue, 7):
    print(turn)

## Завдання 5: «Де загубилось теля?» — ліниве читання
def find_calf(log):
    for line in log:
        if "прив'язав" in line or "прив'язала" in line:
            yield line
            return

journal = [
    "Михайлик отримав доручення",
    "Михайлик передав Василькові",
    "Василько загрався",
    "Василько передав Оленці",
    "Оленка прив'язала теля біля хліва",
    "Оленка пішла додому",
    "Дід заспокоївся",
]

result = next(find_calf(journal))
print(result)