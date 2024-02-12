# Рецептурный сайт

Этот проект представляет собой веб-приложение для обмена рецептами. Пользователи могут создавать свои рецепты, редактировать их, а также просматривать и комментировать рецепты других пользователей.

## Установка

1. **Клонирование репозитория:**

   ```bash
   git clone <https://github.com/bonew1988/Final_django.git>
2. **Создание виртуального окружения:**
   ```bash
   python -m venv venv
3. **Активация виртуального окружения:**
 
* Windows:
   ```bash
    .\venv\Scripts\activate
* Linux/Mac:
   ```bash
    source venv/bin/activate
4. **Установка зависимостей:**
   ```bash
   pip install -r requirements.txt
5. **Применение миграций:**
   ```bash
   python manage.py migrate
6. **Открытие веб-браузера:**
   
* Перейдите по адресу:  <http://127.0.0.1:8000/>.
* Сайт опубликован по адресу:  <https://gb.bonew.ru/>.

## Использование
* Главная страница (/): Стартовая страница.
* Создание/Редактирование рецепта: Перейдите на страницу создания нового рецепта (/recipe/edit/) или редактирования существующего, указав его идентификатор (/recipe/edit/<recipe_id>/).
* Просмотр всех рецептов (/recipe/list/): Показывает список всех рецептов.
* Подробности рецепта (/recipe/<recipe_id>/): Показывает подробности конкретного рецепта.
* Регистрация (/register/): Страница регистрации нового пользователя.
* Вход (/login/): Страница входа пользователя.
* Выход (/logout/): Страница выхода пользователя.

## Зависимости
```bash
asgiref==3.7.2
click==8.1.7
djando==0.2
Django==5.0.2
django-cors-headers==4.3.1
gunicorn==21.2.0
h11==0.14.0
packaging==23.2
pillow==10.2.0
sqlparse==0.4.4
typing_extensions==4.9.0
uvicorn==0.27.1
