
from pathlib import Path  # Імпортуємо інструмент для роботи з файлами
from bs4 import BeautifulSoup  # Імпортуємо BeautifulSoup

html_path = Path(__file__).with_name("products.html")  # Шлях до HTML-файлу
html = html_path.read_text(encoding="utf-8")  # Читаємо вміст файлу

soup = BeautifulSoup(html, "html.parser")  # Розбираємо HTML

title = soup.find("h1")  # Знаходимо перший заголовок h1

print(title.get_text(strip=True))  # Виводимо текст заголовка


# Знаходимо div із класом product, у якому містяться товари
product_block = soup.find("div", class_="product")

# Шукаємо всі span із класом title всередині блоку товарів
titles = product_block.find_all("span", class_="title")

# Шукаємо всі span із класом price всередині блоку товарів
prices = product_block.find_all("span", class_="price")

# zip об'єднує кожну назву з відповідною ціною
for title, price in zip(titles, prices):

    # Отримуємо текст назви без пробілів і переносів
    name = title.get_text(strip=True)

    # Отримуємо текст ціни без пробілів
    product_price = price.get_text(strip=True)

    # Виводимо інформацію про товар
    print(f"Товар: {name}, ціна: {product_price}")
