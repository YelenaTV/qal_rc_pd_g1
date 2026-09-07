class Cossack:
    """ опис козака Війська Запорізького"""
    def __init__(self, name:str, kurin: str, weapons = None):
        """ приймає:
            * ім'я
            * курінь
            * список зброї (за замовчуванням — порожній список)
        """
        self.name = name
        self.kurin = kurin
        #список того, чим озброєний, якщо зброї немає - порожній список
        self.weapons = weapons if (weapons is not None) else []
        #кількість перемог
        self.victories = 0 

    def arm(self, weapon:str):
        """ * додає зброю до арсеналу козака
            * якщо така зброя вже є — повертає `"<ім'я> вже має <зброя>!"`
        """
        if weapon in self.weapons:
            return f"{self.name} вже має {self.weapon}"
        self.weapons.append(weapon)

    def win_battle(self, enemy):
        """* збільшує лічильник перемог на 1
            * повертає `"<ім'я> переміг <ворог>! Слава козаку!"`
        """
        self.victories+=1
        return f"{self.name} переміг {enemy} Слава козаку!"

    def __str__(self):
        #Козак <ім'я> | Курінь: <курінь> | Перемоги: <victories> | Зброя: <зброя через кому>
        return f"Козак {self.name} | Курінь: {self.kurin} | Перемоги: {self.victories} | Зброя: {', '. join(self.weapons)} " 

class ZaporozhianSich:
    #Січ має:* **назву** (`name`)* **список козаків** (`cossacks`)* **максимальну кількість козаків** (`capacity`)
    def __init__(self, name, capacity):
        self.name = name
        #список козаків
        self.cossacks = []
        #максимальну кількість козаків
        self.capacity = capacity

    def enlist(self, cossack):
        """
         **`enlist(cossack)`**
        * приймає об'єкт класу `Cossack` і додає його до Січі
        * якщо місць немає — повертає `"Січ переповнена!"`
        * якщо такий козак вже є — повертає `"<ім'я> вже на Січі!"`
        """
        if len(self.cossacks) >= self.capacity:
            return "Січ переповнена!"
        for is_cossack in self.cossacks:
            if is_cossack.name == cossack.name:
                return f"{cossack.name} вже на Січі!"
        self.cossacks.append(cossack)

    def dismiss (self, name):
        """ **`dismiss(name)`**
            * видаляє козака за ім'ям
            * якщо не знайдено — `"Козака <ім'я> не знайдено!"`
        """
        for cossack in self.cossacks:
            if cossack == name:
                self.cossacks.remove(cossack)
                return
        return f" Козака {name} не знайдено!"
    
    def call_to_battle(self, enemy):
        """* якщо козаків немає — `"Нікому боронити Січ!"`
           * інакше — `"Військо Запорозьке виступає проти <ворог>! У поході <кількість> козаків!"
        """
        if not self.cossacks:
            return "Нікому боронити Січ!"
        return f"Військо Запорозьке виступає проти {enemy}! У поході {len(self.cossacks)} козаків!"

    def best_warrior(self):
        """
            * повертає козака з найбільшою кількістю перемог
            * якщо козаків немає — `"Січ порожня!"`
        """
        if not self.cossacks:
            return "Січ порожня!"

        best = self.cossacks[0]

        for cossack in self.cossacks:
            if cossack.victories > best.victories:
                best = cossack
        return best

    def roster(self):
        """ * повертає список імен усіх козаків
            * якщо порожньо — `"На Січі нікого немає"`
        """
        if not self.cossacks:
            return "На Січі нікого немає"
        names = []
        for cossack in self.cossacks:
            names.append(cossack.name)
        return names
cossack = Cossack("Іван Сірко", "Кальміуський")

cossack.arm("шабля")
cossack.arm("мушкет")
print(cossack.win_battle("яничари"))
print(cossack)
sich = ZaporozhianSich("Чортомлицька Січ", capacity=3)

ivan = Cossack("Іван Сірко", "Кальміуський")
petro = Cossack("Петро Сагайдачний", "Канівський")

ivan.win_battle("яничари")
ivan.win_battle("татари")
petro.win_battle("поляки")

sich.enlist(ivan)
sich.enlist(petro)

print(sich.call_to_battle("турки"))
print(sich.best_warrior())
print(sich.roster())