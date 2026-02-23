# -*- coding: utf-8 -*-
{
    "name": "Library Management",
    "version": "1.0",
    "summary": "Система керування бібліотекою та орендою книг",
    "category": "Services",
    "author": "Твоє Ім’я",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/book_views.xml",
        "views/rent_views.xml",
        "wizard/rent_wizard_views.xml",
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
