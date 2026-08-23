## **Завдання 1: Клас “Квестова Кімната”**

class QuestRoom:
    def __init__(self, name, difficult, player_limit):
        """
        Конструктор класу QuestRoom.
        :param name: назва кімнати
        :param difficulty: рівень складності (1–5)
        :param player_limit: максимальна кількість гравців
        """
        self.name = name
        if (1<= difficult <= 5):
            self.difficult = difficult
        else: 
            raise ValueError("Рівень складності difficulty повинен бути від 1 до 5 ")
        if player_limit >= 0:
            self.player_limit = player_limit
        else:
            raise ValueError("Максимальна кількість гравців має бути додатнім!")
        self.players = []
        self.status = "waiting"
        self.event_log = []

    def add_player(self, name):
        """
        метод **add_player(name)**

        * додає гравця до кімнати
        * якщо місць немає — повертає повідомлення `"No free slots!"
        """
        if len(self.players) >=self.player_limit:
            return "No free slots!"
        self.players.append(name)
        self.event_log.append(f"Player {name} joined")
        return f"Гравця {name} додано!"

    def remove_player(self,name):
        """
        Видаляє гравця зі списку.

        Якщо гравця немає, повертає:
        "Player not found!"
        """
        if name not in self.players:
            return f"Гравця {name} not found!"
        self.players.remove(name)
        self.event_log.append(f"Player {name} left")
        return f"Гравця {name} видалено!"

    def is_full(self):
        """
        Перевіряє, чи заповнена кімната.
        """
       # if (len(self.players) >= self.player_limit):
       #     return "Кімната заповнена!"

        return len(self.players) >= self.player_limit
    #"Є вільні місця"

    def free_slots(self):
        """
        Повертає кількість вільних місць.
        """
        return self.player_limit - len(self.players)
    #f" Вільно {self.player_limit - len(self.players)} слотів"

    def reset_room(self):
        """
        Завершує поточну гру, очищає гравців
        і повертає кімнату до стану очікування.
        """
        self.status = "finished"
        self.event_log.append("Room reset")

        self.players.clear()
        self.status = "waiting"
        return "Room reset"
    
    def players_list(self):
        """
        Повертає список гравців.

        Якщо кімната порожня, повертає:
        "No players in the room"
        """
        if not self.players:
            return "No players in the room"
        return self.players
    
    def start(self):
        """
         метод **start()**

        * якщо кімната пуста → `"Room is empty!"`
        * інакше → `"Quest '<назва>' started with <кількість гравців> players!"`
        """
        if not self.players:
            return "Room is empty!"
        self.status = "active"
        self.event_log.append("Quest started")
        return f"Quest '{self.name}' started with {len(self.players)} players!"
    def show_log(self):
        """
        Повертає історію всіх подій.
        """
        return self.event_log
    def __str__(self):
        """ Метод **\_\_str\_\_**()** для красивого виводу:

        """
        """
        QuestRoom: <name> | Difficulty: <level> | Players: <players_count>/<limit>
        """
        return f"QuestRoom: '{self.name}' | Difficulty: {self.difficult} | Players: {len(self.players)}/{self.player_limit}"


room = QuestRoom("Піратський острів", 3, 4)

print(room)  
print(room.status)
print(room.players_list())
print(room.show_log)

print(room.add_player("Олег"))
print(room.add_player("Даша"))

print(room.players_list())

print(room.free_slots())

print(room.is_full())

print(room.start())

print(room.status)

print(room.remove_player("Олег"))

print(room.remove_player("Sasha"))

print(room.free_slots())

print(room.show_log())

print(room.reset_room())

print(room.status)
print(room.players_list())
print(room.show_log())

print(room)