
import requests  # Імпортуємо бібліотеку для виконання HTTP-запитів

BASE_URL = "https://jsonplaceholder.typicode.com"  # Базова адреса API


# ===== ЗАВДАННЯ 1. ОТРИМАТИ ВСІ POSTS =====

response = requests.get(f"{BASE_URL}/posts", timeout=10)  # Надсилаємо GET-запит для отримання всіх постів
assert response.status_code == 200  # Перевіряємо, що сервер повернув статус 200 (успіх)

posts = response.json()  # Перетворюємо JSON-відповідь на Python-об'єкт
assert isinstance(posts, list)  # Перевіряємо, що отримали список
assert len(posts) == 100  # Перевіряємо, що список містить рівно 100 постів

print("Завдання 1 пройдено: отримано 100 постів")  # Виводимо повідомлення про успіх


# ===== ЗАВДАННЯ 2. ОТРИМАТИ POST З ID=10 =====

response = requests.get(f"{BASE_URL}/posts/10", timeout=10)  # Запитуємо пост із номером 10
assert response.status_code == 200  # Перевіряємо успішний статус відповіді

post = response.json()  # Перетворюємо JSON на словник Python
assert post["id"] == 10  # Перевіряємо, що ID отриманого поста дорівнює 10

required_fields = ["userId", "id", "title", "body"]  # Створюємо список обов'язкових полів

for field in required_fields:  # По черзі перебираємо назви всіх обов'язкових полів
    assert field in post  # Перевіряємо, що поточне поле присутнє у словнику post

print("Завдання 2 пройдено: post 10 містить усі поля")  # Повідомляємо результат


# ===== ЗАВДАННЯ 3. TODOS КОРИСТУВАЧА 2 =====

params = {"userId": 2}  # Створюємо параметр фільтрації за користувачем 2

response = requests.get(f"{BASE_URL}/todos", params=params, timeout=10)  # Надсилаємо GET із параметром userId=2
assert response.status_code == 200  # Перевіряємо статус 200

todos = response.json()  # Отримуємо список завдань користувача
assert isinstance(todos, list)  # Перевіряємо, що результат є списком
assert len(todos) > 0  # Перевіряємо, що список не порожній

for todo in todos:  # Перебираємо кожне завдання зі списку
    assert todo["userId"] == 2  # Перевіряємо, що кожне завдання належить користувачу 2

print("Завдання 3 пройдено: усі todos належать userId=2")  # Виводимо результат


# ===== ЗАВДАННЯ 4. CREATE ЧЕРЕЗ POST =====

payload = {  # Створюємо словник із даними нового поста
    "title": "My first API test",  # Назва нового поста
    "body": "I am learning Python requests",  # Текст нового поста
    "userId": 1  # Номер користувача, який створює пост
}

response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)  # Надсилаємо POST-запит із JSON-даними
assert response.status_code == 201  # Перевіряємо статус 201 (ресурс створено)

created_post = response.json()  # Отримуємо дані створеного поста
assert created_post["title"] == payload["title"]  # Порівнюємо назву з відправленою
assert created_post["body"] == payload["body"]  # Порівнюємо текст із відправленим
assert created_post["userId"] == payload["userId"]  # Перевіряємо номер користувача
assert "id" in created_post  # Перевіряємо, що сервер повернув ID нового поста
assert isinstance(created_post["id"], int)  # Перевіряємо, що ID є цілим числом

print("Завдання 4 пройдено: створено post", created_post["id"])  # Виводимо згенерований ID


# ===== ЗАВДАННЯ 5. UPDATE ЧЕРЕЗ PUT =====

updated_data = {  # Створюємо словник для повного оновлення поста
    "id": 5,  # ID поста, який потрібно оновити
    "title": "Updated title",  # Нова назва
    "body": "Updated body",  # Новий текст
    "userId": 1  # Номер користувача
}

response = requests.put(f"{BASE_URL}/posts/5", json=updated_data, timeout=10)  # Надсилаємо PUT-запит для поста 5
assert response.status_code == 200  # Перевіряємо успішне оновлення

updated_post = response.json()  # Перетворюємо відповідь на словник
assert updated_post["id"] == updated_data["id"]  # Перевіряємо ID
assert updated_post["title"] == updated_data["title"]  # Перевіряємо нову назву
assert updated_post["body"] == updated_data["body"]  # Перевіряємо новий текст
assert updated_post["userId"] == updated_data["userId"]  # Перевіряємо номер користувача

print("Завдання 5 пройдено: PUT повернув оновлені дані")  # Виводимо результат


# ===== ЗАВДАННЯ 6. PARTIAL UPDATE ЧЕРЕЗ PATCH =====

patch_data = {"title": "Patched title"}  # Створюємо словник лише з полем, яке змінюємо

response = requests.get(f"{BASE_URL}/posts/5", timeout=10)  # Отримуємо початковий стан поста 5
assert response.status_code == 200  # Перевіряємо, що початковий пост доступний
original_post = response.json()  # Зберігаємо початкові дані поста

response = requests.patch(f"{BASE_URL}/posts/5", json=patch_data, timeout=10)  # Надсилаємо PATCH лише з новою назвою
assert response.status_code == 200  # Перевіряємо статус успіху

patched_post = response.json()  # Отримуємо відповідь після часткового оновлення
assert patched_post["title"] == patch_data["title"]  # Перевіряємо нову назву
assert patched_post["id"] == original_post["id"]  # Перевіряємо, що ID не змінився
assert patched_post["body"] == original_post["body"]  # Перевіряємо, що текст залишився старим
assert patched_post["userId"] == original_post["userId"]  # Перевіряємо, що користувач не змінився

print("Завдання 6 пройдено: PATCH змінив тільки title")  # Виводимо результат


# ===== ЗАВДАННЯ 7. DELETE =====

response = requests.delete(f"{BASE_URL}/posts/5", timeout=10)  # Надсилаємо запит на видалення поста 5
assert response.status_code in [200, 204]  # Перевіряємо, що сервер повернув 200 або 204

print("Завдання 7 пройдено: DELETE повернув успішний статус")  # Виводимо результат


# ===== ЗАВДАННЯ 8. НЕІСНУЮЧИЙ POST =====

response = requests.get(f"{BASE_URL}/posts/999999", timeout=10)  # Запитуємо пост із неіснуючим ID

assert response.status_code == 404 or (  # Приймаємо статус 404 або успішну порожню відповідь
    response.status_code == 200 and response.json() in ({}, [], None)  # Для 200 перевіряємо порожній JSON
)

print("Завдання 8 пройдено: неіснуючий post оброблено")  # Виводимо результат


# ===== ЗАВДАННЯ 9. POST БЕЗ ПОЛІВ =====

empty_payload = {}  # Створюємо порожній словник без полів

response = requests.post(f"{BASE_URL}/posts", json=empty_payload, timeout=10)  # Надсилаємо POST із порожнім JSON

print("Завдання 9. Статус:", response.status_code)  # Виводимо фактичний HTTP-статус
print("Завдання 9. Відповідь:", response.text)  # Виводимо тіло відповіді сервера

assert response.status_code in [200, 201, 400, 422]  # Перевіряємо один із можливих статусів
# Для цього завдання головне — дослідити фактичну поведінку API


# ===== ЗАВДАННЯ 10. CUSTOM HEADERS =====

headers = {"User-Agent": "QA Student"}  # Створюємо власний HTTP-заголовок User-Agent

response = requests.get(f"{BASE_URL}/posts", headers=headers, timeout=10)  # Надсилаємо GET із заголовком
assert response.status_code == 200  # Перевіряємо успішне виконання запиту
assert response.request.headers["User-Agent"] == "QA Student"  # Перевіряємо відправлений заголовок

print("Завдання 10 пройдено: custom header передано")  # Виводимо результат


print("Усі 10 перевірок завершено!")  # Фінальне повідомлення після всіх перевірок
