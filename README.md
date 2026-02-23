# 🛠 Стек технологій
- ERP: Odoo 18.0 Community Edition 
- Language: Python 3.13
- Database: PostgreSQL 17
- Deployment: Docker / Docker Compose
- Code Style: Black, Flake8 (PEP8)


# Library Management Module for Odoo 18

## Як запустити
1. Розпакуйте архів.
2. У терміналі виконайте: `docker-compose up --build`
3. Відкрийте `http://localhost:8069`
4. Створіть базу `test_odoo` (якщо не створилася автоматично).
5. Активуйте Developer Mode.
6. Встановіть модуль `library_management`.

## Особливості
- Реалізовано REST API за адресою `/library/books`.
- Використано нові стандарти Odoo 18 (`<list>` замість `<tree>`).
- Код повністю прокоментований згідно з вимогами.
- 
### Налаштування бази даних:
- Відкрийте в браузері: http://localhost:8069
- Створіть базу даних з назвою test_odoo.
- Логін/пароль адміністратора встановіть на свій розсуд (admin/admin).

### Активація модуля:
- Перейдіть у Settings -> Activate the developer mode.
- Перейдіть у меню Apps -> натисніть Update Apps List.
- Знайдіть модуль Library Management та натисніть Activate.

# 📖 Функціонал модуля
**Керування книгами**: Створення, редагування та відстеження статусу доступності.

**Процес оренди**: - Використання Wizard (спливаючого вікна) для швидкої видачі книги.

**Автоматична зміна статусу** is_available при створенні/закритті оренди.

**Валідація**: Python-constraints на рівні моделі, що забороняють видавати одну й ту саму книгу двічі.

**REST API**: Публічний ендпоінт для отримання актуального каталогу книг.

# 🌐 REST API

Ендпоінт: ` GET /library/books `

Приклад відповіді:
```
JSON
[
  {
    "id": 1,
    "name": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "is_available": false,
    "published_date": "1925-04-10"
  }
]
```

# 🧪 Якість коду
**Для дотримання стандартів PEP8 у проекті налаштовані:**

- Black: Форматування коду (line-length: 79).

- Flake8: Лінтування та перевірка складності.

- Конфігураційні файли pyproject.toml та .flake8 знаходяться у корені проекту.

# 📂 Структура проекту
```
library_project/
├── addons/               # Custom module
│   ├── __init__.py
│   └──  library_management
│       ├── __manifest__.py
│       ├── __init__.py
│       ├── models/
│       │   ├── book.py
│       │   ├── rent.py
│       │   └── __init__.py
│       ├── views/
│       │   ├── book_views.xnl
│       │   ├── rent_views.xnl
│       │   └── __init__.py
│       ├── security/
│       │   ├── ir.model.access.csv
│       │   └── __init__.py
│       ├── wizard/
│       │   ├── rent_wizard.py
│       │   ├── rent_wizard_views.xml
│       │   └── __init__.py
│       └── controllers/
│           └── __init__.py
│   
├── config/               # Configuration Odoo
│   └── odoo.conf
└── docker-compose.yml
```
