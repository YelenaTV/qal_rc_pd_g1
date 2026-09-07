from abc import ABC, abstractmethod
class MagicCreature(ABC):
    def __init__(self, name: str, magic_level: int, health:int):
        self.name = name    #**ім'я** (`name`)
        self._validate_magic_level(magic_level)
        self._magic_level = magic_level  #**рівень магії** (`_magic_level`) — від 1 до 10, **захищений** атрибут
        self.__validate_health(health)  
        self.__health = health            #**здоров'я** (`__health`) — від 0 до 100, **приватний** атрибут
        self.__alive = health > 0          #Якщо здоров’я більше нуля — істота жива.

    # перевірка рівня магії
    def _validate_magic_level(self, value:int):
        if isinstance(value, int) and 1<= value <= 10:
            return
        else:
            raise ValueError("Рівень магії має бути від 1 до 10!")
    
    # перевірка здоров'я
    def __validate_health(self, value:int):
        if isinstance(value, int) and 0<= value <= 100:
            return
        else: 
            raise ValueError("Здоров'я має бути від 0 до 100!")

    @property
    def magic_level(self):           # геттер для рівня магії
        return self._magic_level     # повертаємо значення
    
    @magic_level.setter
    def magic_level(self, value:int):       # сеттер для рівня магії
        self._validate_magic_level(value)   # перевіряємо значення
        self._magic_level=value             # записуємо нове значення

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value: int):   # сеттер для здоров'я
        self.__validate_health(value)  # спочатку перевірка
        if value<=0 :               # якщо здоров'я 0 або менше
            self.__health = 0       # ставимо 0
            self.__alive = False    # істота мертва
        else:                       # якщо значення нормальне
            self.__health = value   # записуємо нове здоров'я
            self.__alive = True     # істота жива

    @property
    def is_alive(self):             # властивість "чи жива істота"
        return self.__alive          # повертаємо True або False

    def take_damage(self, amount:int): # метод для отримання шкоди
        if not self.__alive:            # якщо істота вже мертва
            return f"{self.name} вже переміг смерть ... або ні"
        self.health = self.__health - amount  # віднімаємо шкоду через setter
    @abstractmethod
    def use_ability(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    def __str__(self):
        return f"{self.name} | Магія: {self._magic_level} | НР: {self.__health} | Живий: {self.__alive}"

    
## Завдання 2: Підкласи казкових істот
# підклас мольфара.
class Molfar(MagicCreature): 
    def __init__(self, name: str, magic_level: int, health: int, element: str, spells: int):
        super().__init__(name, magic_level, health) #запускає конструктор батьківського класу
        self.element = element #**стихія** (`element`) — наприклад, `"вогонь"`, `"вода"`, `"вітер"`, `"земля"
        self.spells = spells #**запас заклинань** (`__spells`) — ціле число, початкове значення задається при створенні

    @property
    def spells(self):
        return self.__spells

    @spells.setter
    def spells(self, value: int):
        if isinstance(value, int) and value >= 0:
            self.__spells = value
        else: 
            raise ValueError("Кількість заклинань має бути невід'ємною") 

    def use_ability(self):
        if self.__spells > 0:
            self.spells = self.spells-1
            return(f"{self.name} використовує стихію {self.element}." 
                   f"Залишилось заклинань: {self.__spells}")
        return f"{self.name} більше немає заклинань."

    def describe(self):
        return (
            f"Мольфар {self.name}, стихія: {self.element}, "
            f"магія: {self.magic_level}, НР: {self.health}. "
            f"Живий: {self.is_alive}"
        )

### 🌊 Клас `Rusalka` (Русалка)
class Rusalka(MagicCreature): #Русалка — небезпечна водяна істота, що принаджує мандрівників.
    def __init__(self, name: str, magic_level:int, health: int, river:str, charm_power: int):
        super().__init__(name, magic_level, health)    
        self.river = river  #**річка** (`river`) — де мешкає
        self.charm_power = charm_power #**__charm_power** — сила чар від 1 до 5, **приватний** атрибут

    @property
    def charm_power(self):
        return self.__charm_power

    @charm_power.setter #**Property `charm_power`** із геттером та сеттером (діапазон 1–5, інакше `ValueError`)
    def charm_power(self, value: int):
        if isinstance(value, int) and (1<= value <= 5):
            self.__charm_power= value
        else: 
            raise ValueError("Сила чар має бути від 1 до 5")
    
    def use_ability(self):
        message= f"Русалка {self.name} з річки {self.river} зачаровує мандрівника! Сила чар: {self.__charm_power}"
        if self.__charm_power == 5:
            message= message + " Ніхто не встоїть!"
        return message

    def describe(self):
        return f"Русалка {self.name}, мешканка річки {self.river}. Сила чар: {self.__charm_power}/5"
    
### 🐺 Клас `Perelesnyk` (Перелесник)
class Perelesnyk(MagicCreature):  #ерелесник — вогняний дух, що літає між світами.
    def __init__(self, name: str, magic_level: int, health: int, speed: int, form: str):
        super().__init__(name, magic_level, health)

        self.speed = speed # **швидкість польоту** (`__speed`) — від 1 до 100, **приватний** атрибут

        self.form = form  #**форма** (`form`) — `"вогняна куля"` або `"людська"`, змінюється методом

    @property
    def speed(self):
        return self.__speed
    #**Property `speed`** із геттером та сеттером (діапазон 1–100)
    @speed.setter
    def speed(self, value: int):
        if isinstance(value, int) and (1<= value <=100):
            self.__speed = value
        else:
            raise ValueError("Швидкість має бути від 1 до 100")

    def change_form(self):
        # **Метод `change_form()`** — перемикає між `"вогняна куля"` та `"людська"` і повертає `"Перелесник перетворився на <нова форма>!"`
        self.form = "людська" if self.form =="вогняна куля" else "вогняна куля"
        return f"Перелесник перетворився на {self.form}!"
    
    def use_ability(self):
        message = f"Перелесник {self.name} мчить крізь ніч зі швидкістю {self.__speed}! Форма: {self.form}"
        if self.form == "людська":
            message= message + " Ніхто не здогадається..."
        return message

    def describe(self):
        return f"Перелесник {self.name}. Швидкість: {self.__speed}. Зараз у формі: {self.form}"

## Завдання 3: Клас `EnchantedForest`
class EnchantedForest: #Це клас лісу.
    def __init__(self, name: str, capacity: int):
        self.name = name #**назва лісу** (`name`)
        self.capacity = capacity #**максимальна кількість мешканців** 
        self.__creatures = [] #**список істот** (`__creatures`) — **приватний**

    def add_creature(self, creature): #**`add_creature(creature)`**
        if not isinstance(creature, MagicCreature):
            raise TypeError("Можна додавати лише MagicCreature")  #приймає об'єкт підкласу `MagicCreature`
        if len(self.__creatures) >= self.capacity: #якщо місць немає — `"Зачарований ліс <name> переповнений!"`
            return f"Зачарований ліс {self.name} переповнений!"
        if not creature.is_alive:                 #якщо істота мертва — `"Мертві істоти не можуть оселитись у лісі!"`
            return "Мертві істоти не можуть оселитись у лісі!"
        for exis_creature in self.__creatures:
            if exis_creature.name == creature.name: #якщо вже є — `"<ім'я> вже мешкає у цьому лісі!"`
                return f"{creature.name} вже мешкає у цьому лісі!"
        self.__creatures.append(creature)    
    def remove_creature(self, name): # * видаляє за ім'ям
                                    #* якщо не знайдено — `"Істоту <name> не знайдено у лісі!"`
        for creature in self.__creatures:
            if creature.name == name:
                self.__creatures.remove(creature)
                return f"{name} залишив ліс {self.name}"
        return f"Істоту {name} не знайдено у лісі!"

    def most_powerful(self): #Цей метод знаходить у лісі істоту з найвищим рівнем магії.
        if not self.__creatures:
            return "Ліс порожній"
        strong_istota = self.__creatures[0]

        for creature in self.__creatures:
            if creature.magic_level > strong_istota.magic_level:
                strong_istota = creature
        return strong_istota
    #Цей метод змушує всіх живих істот лісу атакувати незваного гостя.
    def attack_intruder(self, intruder_name):
        alive_creatures = []  #порожній список для живих істот.

        for creature in self.__creatures:
            if creature.is_alive:
                alive_creatures.append(creature)

        if not alive_creatures:
            return f"Ліс беззахисний перед {intruder_name}!"

        results = []

        for creature in alive_creatures:
            results.append(creature.use_ability()) #* кожна жива істота у лісі викликає свій `use_ability()`

        return results #результат — список рядків від кожної істоти

    def census(self):
        if not self.__creatures:  #якщо порожній — `"Ліс порожній"`
            return "Ліс порожній"

        descriptions = []

        for creature in self.__creatures:
            descriptions.append(creature.describe()) 
        return descriptions #повертає список рядків через `describe()` кожної істоти

    @property  #тільки геттер — кількість живих істот у лісі
    def creatures_count(self):
        count = 0

        for creature in self.__creatures:
            if creature.is_alive:
                count = count + 1

        return count          
        
forest = EnchantedForest("Чорний Ліс", capacity=5)

molfar = Molfar("Юрій", magic_level=8, health=90, element="вогонь", spells=3)
rusalka = Rusalka("Калина", magic_level=6, health=100, river="Дніпро", charm_power=5)
perelesnyk = Perelesnyk("Іскра", magic_level=7, health=85, speed=95, form="вогняна куля")

forest.add_creature(molfar)
forest.add_creature(rusalka)
forest.add_creature(perelesnyk)

print(forest.most_powerful())
print(forest.attack_intruder("мисливець"))

molfar.take_damage(90)
print(f"Стан :{molfar.is_alive}")

print(forest.census())