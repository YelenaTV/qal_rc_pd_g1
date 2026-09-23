import csv
from pathlib import Path

#Прочитайте CSV-файли "users_1.csv" та "users_2.csv".
def read_file(filepath: Path) -> list[dict]:
    with open(filepath, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

#записати список словників у CSV-файл із заголовком.
def write_csv(filepath: Path, content: list[dict]) -> None:#шлях до файлу, куди записувати, content — список словників (рядків), які треба записати.
    if not content:  #Якщо content порожній — створює порожній файл.
        filepath.write_text("", encoding="utf-8")  
        return

    fieldnames = list(content[0].keys())  # Бере ключі першого словника як назви колонок: fieldnames = list(content[0].keys())
    with open(filepath, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)  #Створює DictWriter з цими fieldnames.
        writer.writeheader()  #записує заголовок (назви колонок)
        writer.writerows(content) #записує всі рядки.

#знайти дублікати у списку рядків і повернути (унікальні рядки, кількість дублікатів).
def find_duplicates(rows: list[dict]) -> tuple[list[dict], int]:
    seen = set()
    unique_rows = []  #список унікальних рядків (словників);
    duplicate_count = 0  #скільки разів зустрілися дублікати.

    for row in rows:
        key = tuple(sorted(row.items()))  # перетворюємо словник на хешований кортеж
        if key in seen:  #Якщо key вже є в seen → це дублікат, збільшує лічильник duplicate_count += 1.
            duplicate_count += 1
        else:  #Якщо key ще немає в seen → додає його в seen і сам рядок у список unique_rows.
            seen.add(key)
            unique_rows.append(row)

    return unique_rows, duplicate_count


def main() -> None:
    base = Path(__file__).parent

    # Читаємо обидва файли
    data_1 = read_file(base / "users_1.csv")
    data_2 = read_file(base / "users_2.csv")

    # Об'єднуємо всі рядки
    all_rows = data_1 + data_2

    # Знаходимо унікальні рядки та кількість дублікатів
    unique_rows, duplicate_count = find_duplicates(all_rows)

    # Записуємо результат
    out_path = base / "clean_users_3.csv"
    write_csv(out_path, unique_rows)

    # Виводимо статистику
    print(f"Знайдено дублікатів: {duplicate_count}")
    print(f"Унікальних записів збережено: {len(unique_rows)}")
    print(f"Файл: {out_path}")


if __name__ == "__main__":
    main()