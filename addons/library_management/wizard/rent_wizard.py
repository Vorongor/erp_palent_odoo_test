# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LibraryRentWizard(models.TransientModel):
    """
    Тимчасова модель (TransientModel) для оформлення видачі книги.
    Дані цієї моделі не зберігаються в БД назавжди і
    очищаються системою автоматично.
    Використовується для створення зручного діалогового вікна.
    """

    _name = "library.rent.wizard"
    _description = "Library Rent Wizard"

    # Поле Many2one для зв'язку з книгою.
    # Значення сюди передається автоматично через контекст з форми книги.
    book_id = fields.Many2one("library.book", string="Book", required=True)

    # Вибір клієнта, якому видається книга
    partner_id = fields.Many2one("res.partner", string="Client", required=True)

    def action_confirm_rent(self):
        """
        Метод підтвердження оренди.
        Створює постійний запис у моделі library.rent та оновлює статус книги.
        """
        # Перевірка на роботу з одним записом
        self.ensure_one()

        # Використовуємо self.env для створення запису в моделі оренди.
        self.env["library.rent"].create(
            {
                "book_id": self.book_id.id,
                "partner_id": self.partner_id.id,
            }
        )

        # Пряме оновлення поля книги через метод write.
        # Хоча в моделі library.rent ми вже перевизначили метод create,
        # явне оновлення тут гарантує консистентність даних.
        self.book_id.write({"is_available": False})

        # Повертаємо дію закриття вікна після успішного завершення
        return {"type": "ir.actions.act_window_close"}
