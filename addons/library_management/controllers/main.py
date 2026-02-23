# -*- coding: utf-8 -*-
import json

from odoo import http
from odoo.http import request


class LibraryController(http.Controller):
    """
    Контролер для обробки зовнішніх API-запитів до бібліотечної системи.
    Використовуємо http.Controller, оскільки Odoo не має вбудованого
    REST фреймворку типу DRF, тому маршрутизація та формування
    JSON-відповідей робиться вручну.
    """

    @http.route(
        "/library/books",
        type="http",
        auth="public",
        methods=["GET"],
        csrf=False,
    )
    def get_books(self, **kwargs):
        """
        Ендпоінт для отримання списку всіх книг.
        - type="http":
            вказує, що ми повертаємо стандартну HTTP-відповідь (а не JSON-RPC).
        - auth="public":
            дозволяє доступ без авторизації (згідно з завданням).
        - csrf=False:
            відключаємо CSRF-захист, оскільки це GET-запит для API.
        """

        # Використовуємо .sudo(), щоб обійти обмеження прав доступу,
        # оскільки запит може прийти від неавторизованого 'public' користувача.
        # .search([]) повертає всі записи моделі library.book.
        books = request.env["library.book"].sudo().search([])

        # Формуємо список словників для подальшої серіалізації в JSON
        book_data = []
        for book in books:
            book_data.append(
                {
                    "id": book.id,
                    "name": book.name,
                    "author": book.author or "Unknown",
                    "is_available": book.is_available,
                    "published_date": (
                        str(book.published_date)
                        if book.published_date
                        else None
                    ),
                }
            )

        # Повертаємо сформований JSON з правильним заголовком Content-Type.
        # Використовуємо json.dumps для перетворення список у JSON-рядок.
        return request.make_response(
            json.dumps(book_data),
            headers=[("Content-Type", "application/json")],
        )
