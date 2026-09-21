# Імпортуємо модуль для запису повідомлень у лог.
import logging
# Потрібен для паузи між спробами.
import time
from functools import wraps
# повідомлення рівнів INFO, WARNING та ERROR.
logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")

def chronicle(author="Анонімний"):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs): # wrapper замінює оригінальну функцію після декорування.
                                        # *args збирає позиційні аргументи у кортеж.
                                        # **kwargs збирає іменовані аргументи у словник.
            positional_args = [repr(arg) for arg in args] #  Перетворюємо кожен позиційний аргумент у текст. repr() показує рядки разом з лапками.

             # іменовані аргументи у формат: key='value'.
            keyword_args = [f"{key} = {value!r}" for key, value in kwargs.items()]
            arguments = ", ".join(positional_args + keyword_args) #Об'єднуємо всі аргументи через кому та пробіл.
            #  в лог інформацію перед виконанням функції.
            logging.info(f"[Літописець: {author}] " f"Викликано: {func.__name__}({arguments})")

            result = func(*args, **kwargs)
            #  отриманий результат у лог.
            logging.info(f"[Результат]: {result}")

            return result

        return wrapper

    return decorator

@chronicle("Самійло Величко")
def make_decision(action, target):
    return f"Рішення: {action} → {target}"

@chronicle()
def count_warriors(regiment):
    return 500

make_decision("Атакувати", "Перекоп")
count_warriors("Полтавський")


"""### Завдання 2. Хранитель фортеці"""
# повідомлення рівнів INFO, WARNING та ERROR.
logging.basicConfig(level=logging.INFO,format="%(levelname)s %(message)s")

# secret — правильний пароль.
def guard(secret):

    # func — функція, яку потрібно захистити.
    def decorator(func):

        # Зберігаємо ім'я оригінальної функції.
        @wraps(func)

        # перевірка пароля.
        def wrapper(*args, **kwargs):
            password = input("Назви пароль: ")
            if password == secret:
                logging.info( f"Доступ надано: {func.__name__}")

                return func(*args, **kwargs)
            # Записуємо невдалу спробу в лог.
            logging.warning(f"Невдала спроба доступу до: {func.__name__}")

            print("Стій! Доступ заборонено.")

            return None

        return wrapper
    
    return decorator

@guard(secret="Мамай")
def open_treasury():
    print("Скарбниця відчинена!")
    return "золото, срібло, зброя"

result = open_treasury()


### Завдання 3. Залізний характер
# повідомлення рівнів INFO, WARNING та ERROR.
logging.basicConfig( level=logging.INFO,format="%(levelname)s %(message)s")
def retry(times=3, delay=1.0):

    # decorator отримає функцію, яку треба повторювати.
    def decorator(func):

        # Зберігаємо ім'я та іншу інформацію про func.
        @wraps(func)

        # wrapper буде запускати функцію кілька разів.
        def wrapper(*args, **kwargs):

            # Запам'ятовуємо останню помилку.
            last_error = None

            # Створюємо спроби від 1 до times включно.
            for attempt in range(1, times + 1):

                # Пробуємо виконати функцію.
                try:

                    # Запускаємо справжню функцію.
                    result = func(*args, **kwargs)

                    # Якщо помилки немає, записуємо успіх.
                    logging.info(f"Успіх на спробі {attempt}/{times}")

                    # Повертаємо результат.
                    # Після цього нові спроби вже не потрібні.
                    return result

                # Якщо функція викликала помилку, потрапляємо сюди.
                except Exception as error:

                    #  текст останньої помилки.
                    last_error = error

                    #  невдала спроба у WARNING.
                    logging.warning(f"Спроба {attempt}/{times} не вдалася: {error}")

                    # Якщо це не остання спроба, робимо паузу.
                    if attempt < times:
                        time.sleep(delay)

            # Сюди програма потрапить,
            # якщо всі спроби завершилися помилкою.
            logging.error(f"Усі спроби для {func.__name__} завершилися невдало")

            # Повторно викликаємо останню помилку.
            raise last_error

        return wrapper

    return decorator         

import random

@retry(times=4, delay=0.5)
def unreliable_scout():
    if random.random() < 0.7:  # 70% шанс провалу
        raise ConnectionError("Розвідник не повернувся")
    return "Ворог за річкою!"

result = unreliable_scout()
print(result)