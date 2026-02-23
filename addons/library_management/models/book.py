from odoo import models, fields

class LibraryBook(models.Model):
    """
        Основна модель для зберігання інформації про книги.
        Використовується стандартний клас models.Model
        для правильного зберігання в БД.
    """
    _name = "library.book"
    _description = "Library Book"

    # Створюємо моделі відповідно до завдання:
    # name (Char) - обов'язкове,
    # author (Char) – опціонально,
    # published_date (Date) - опціонально,
    # is_available - за замовчуванням True, змінюється автоматично при оренді
    name = fields.Char(string="Book name", required=True)
    author = fields.Char(string="Author")
    published_date = fields.Date(string="Published date")
    is_available = fields.Boolean(string="Is available", default=True)

    def action_open_rent_wizard(self):
        """
        Метод для виклику допоміжного вікна (Wizard).
        Повертає action типу 'ir.actions.act_window', який Odoo інтерпретує як
        команду відкрити спливаюче вікно (target: new).
        Ми передаємо ID поточної книги в контекст, щоб Wizard знав,
        яку книгу ми оформлюємо.
        """
        self.ensure_one()  # Перевірка, що метод викликано для одного запису
        return {
            "name": "Publish a book",
            "type": "ir.actions.act_window",
            "res_model": "library.rent.wizard",
            "view_mode": "form",
            "target": "new",
            "context": {"default_book_id": self.id},
        }