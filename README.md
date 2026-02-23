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