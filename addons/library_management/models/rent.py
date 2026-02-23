from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LibraryRent(models.Model):
    """
    Модель для реєстрації фактів оренди книг.
    Встановлює зв'язки між книгами та партнерами (клієнтами).
    """
    _name = "library.rent"
    _description = "Book Rent"

    # Many to one створює зовнішній ключ (Foreign Key) у таблиці
    partner_id = fields.Many2one("res.partner", string="Client", required=True)
    book_id = fields.Many2one("library.book", string="Book", required=True)

    # readonly=True запобігає ручному редагуванню дати видачі в інтерфейсі
    rent_date = fields.Date(
        string="Дата видачі",
        default=fields.Date.context_today,  # Встановлює поточну дату сервера
        readonly=True
    )
    return_date = fields.Date(string="Return date")

    @api.constrains("book_id", "return_date")
    def _check_book_availability(self) -> None:
        """
        Валідація на рівні Python.
        Перевіряє, щоб не видати книгу, яка вже знаходиться в оренді.
        """
        for record in self:
            # Шукаємо інші записи оренди для цієї ж книги,
            # де поле return_date порожнє
            domain = [
                ("book_id", "=", record.book_id.id),
                ("return_date", "=", False),
                ("id", "!=", record.id),  # Виключаємо поточний запис з пошуку
            ]
            active_rent = self.search(domain)
            if active_rent:
                # Якщо знайдено активний запис — викидаємо помилку помилкою
                raise ValidationError(
                    f'Book "{record.book_id.name}" has already been '
                    "checked out and not yet returned!"
                )

    @api.model
    def create(self, vals):
        """
        Перевизначення методу create для автоматизації зміни статусу книги.
        Коли створюється запис про оренду, ми автоматично позначаємо книгу як
        зайняту.
        """
        # Викликаємо базовий метод super() для створення запису в БД
        res = super(LibraryRent, self).create(vals)
        if res.book_id:
            res.book_id.is_available = False
        return res

    def write(self, vals):
        """
        Перевизначення методу write для відстеження повернення книги.
        Якщо в словнику 'vals' з'являється дата повернення,
        ми оновимо статус книги.
        """
        # Викликаємо базовий метод super() для взаємодії з БД
        res = super(LibraryRent, self).write(vals)
        if 'return_date' in vals and vals['return_date']:
            for record in self:
                record.book_id.is_available = True
        return res
