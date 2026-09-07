"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків, 
де кожен рядок містить числа, розділені комами. Функція повинна повертати список 
із сум чисел для кожного рядка або відповідне повідомлення про помилку у 
випадку некоректних даних.

#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""
import unittest

def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""

    if not isinstance(string_list,list):
        raise ValueError("Вхідні дані повинні бути списком.")
    
    # Перевірка: список не повинен бути порожнім
    if len(string_list) == 0:
        raise ValueError("Список не може бути порожнім.")
    
    result = []
    # Проходимо по кожному елементу списку
    for item in string_list:
        # Якщо елемент не є рядком, повертаємо потрібне повідомлення
        if not isinstance(item, str):
            result.append("Не можу це зробити! AttributeError")
            continue
        try:
            # Розбиваємо рядок по комахах
            parts = item.split(",")
            # Перетворюємо кожну частину в число та рахуємо суму
            total = 0
            for part in parts:
                total = total + int(part)

            result.append(total)
        except ValueError:
            result.append("Не можу це зробити!") ## Якщо в рядку є некоректні символи
    
    return result
class TestSumNumbersInList(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(sum_numbers_in_list(["1,2,3", "4,0,6"]), [6, 10])

    def test_invalid_string(self):
        self.assertEqual(
            sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]),
            [6, "Не можу це зробити!", 10]
        )
    def test_non_string_item(self):
        self.assertEqual(
            sum_numbers_in_list(["1,2,3,4", 7]),
            [10, "Не можу це зробити! AttributeError"]
        )

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            sum_numbers_in_list([])

    def test_not_a_list(self):
        with self.assertRaises(ValueError):
            sum_numbers_in_list("21")

    def test_another_invalid_string(self):
        self.assertEqual(
            sum_numbers_in_list(["4/0,6"]),
            ["Не можу це зробити!"]
        )
if __name__ == "__main__":
    output = sum_numbers_in_list(["1,2,3", "4,0,6"])
    print(output)

    output = sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])
    print(output)
    """
    sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
    sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
    sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
    sum_numbers_in_list([])  # ValueError
    sum_numbers_in_list("21")  # ValueError
    """
    unittest.main()