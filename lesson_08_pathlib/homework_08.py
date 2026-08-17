### Робота з файлами та папками — завдання

from pathlib import Path

def write_file(filepath: Path, content: str):
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

def read_file(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        return content
def append_file(filepath:Path, content) ->str:
   with open(filepath, "a", encoding="utf-8", ) as file:
       file.write(content)

"""1. **Створення файлу**
   Створи текстовий файл `hello.txt` і запиши в нього рядок:

   ```
   Hello, Python!
   ```
"""
# coding here


write_file(Path("lesson_08_pathlib") / "hello.txt", "Hello, Python!")
"""
2. **Читання файлу**
   Відкрий файл `hello.txt` і виведи його вміст на екран.
"""
# coding here

content = read_file(Path("lesson_08_pathlib") / "hello.txt")
print(content)
"""   
3. **Дозапис у файл**
   Додай у файл `hello.txt` ще один рядок:

   ```
   Learning file operations.
   ```
"""
# coding here

append_file(Path("lesson_08_pathlib") / "hello.txt", "\nLearning file operations.")

"""
4. **Читання кількох рядків**
   Виведи всі рядки з файлу `hello.txt` по одному рядку (без додаткових символів `\n`).
"""
# coding here
def read_file_line(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())

read_file_line(Path("lesson_08_pathlib") / "hello.txt")
"""
5. **Підрахунок символів**
   Прочитай файл `hello.txt` і виведи кількість символів у ньому.
"""
# coding here
def count_chars(filepath: Path):
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read().replace("\n", "")
        return len(content)
count = count_chars(Path("lesson_08_pathlib")/ "hello.txt")
print(f" Кількість символів у файлі дорівнює {count}")
"""
6. **Створення папки**
   Створи папку з назвою `data`. Усередині неї створи файл `notes.txt` із текстом:

   ```
   My first note.
   ```
"""
# coding here
data_folder = Path("lesson_08_pathlib") / "data"
data_folder.mkdir(exist_ok=True) #Метод .mkdir() означає «створити папку».
notes_file = data_folder / "notes.txt" #Тут ми створюємо шлях до файлу notes.txt усередині папки data.
write_file(notes_file, "My first note.")#У функцію передаються 

"""
def write_file(filepath: Path, content: str):
    with open(filepath, "w", encoding="utf-8") as file: #відкриває файл для запису.Якщо notes.txt ще не існує, Python його створює.
        file.write(content) # записує текст у вже відкритий файл
"""
"""
7. **Список файлів у папці**
   Виведи на екран список усіх файлів у папці `data`.
"""
# coding here
data_folder = Path("lesson_08_pathlib") / "data"
for file in data_folder.iterdir(): #Переглянути все, що знаходиться всередині папки data
    if file.is_file(): #перевіряємо Чи є поточний об’єкт файлом?
        print(file.name)#повертає тільки назву файлу
"""
8. **Копіювання вмісту**
   Прочитай вміст файлу `notes.txt` і запиши його у файл `copy.txt` (у тій же папці `data`).
"""
# coding here
data_folder = Path("lesson_08_pathlib") / "data"
copy_file = data_folder / "copy.txt" #створюємо шлях до нового файлу lesson_08_pathlib/data/copy.txt
content = read_file(notes_file)
write_file(copy_file,content) #Якщо copy.txt не існує, Python створює його.
                              #Якщо copy.txt уже існує, Python очищає його старий вміст.
                              #copy_file це шлях до нового файлу lesson_08_pathlib/data/copy.txt 
                              # content = "My first note."
"""
def read_file(filepath: Path):
   with open(filepath, "r", encoding="utf-8") as file: #Файл notes.txt відкривається для читання.
      content = file.read() #Метод .read() читає весь текст із файлу.
      return content #змінна content матиме значення "My first note"
def write_file(filepath: Path, content: str): #Path("lesson_08_pathlib/data/copy.txt"),
   "My first note."
   with open(filepath, "w", encoding="utf-8") as file: #відкриває файл для запису.Якщо copy.txt ще не існує, Python його створює.
      file.write(content) # записує текст у вже відкритий файл "My first note."
"""
"""
9. **Об’єднання файлів**
   Створи два файли: `a.txt` і `b.txt`, кожен із будь-яким текстом.
   Запиши їхній вміст у новий файл `ab.txt`.
"""
# coding here
data_folder = Path("lesson_08_pathlib") / "data"
a_file = data_folder / "a.txt"  #отримуємо шлях до файлу: lesson_08_pathlib/data/a.txt
b_file = data_folder / "b.txt"
ab_file = data_folder / "ab.txt"
write_file(a_file, "Random text from file a. \n")
write_file(b_file, "Random text from file b. \n")
a_text = read_file(a_file)
b_text = read_file(b_file)
write_file(ab_file, a_text + b_text)
"""
10. **Пошук слова у файлі**
    У файлі `notes.txt` перевір, чи є слово `"note"`.
    Якщо є — виведи `"Знайдено"`, інакше `"Не знайдено"`.
"""
# coding here
notes_file=Path("lesson_08_pathlib") / "data" / "notes.txt"
content=read_file(notes_file)
if "note" in content: 
    print("Знайдено")
else:
    print("Не знайдено")
