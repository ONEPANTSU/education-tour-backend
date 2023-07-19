from datetime import datetime

from src.event_module.schemas import Address, CategoryRead

CATEGORIES = [
    CategoryRead(id=2, name="День открытых дверей"),
    CategoryRead(id=3, name="Студенческая весна"),
]

EVENTS_CREATE = [
    {
        "name": "Бонч зовёт!",
        "description": "Нам нужен именно ты :)",
        "date_start": datetime(year=2023, month=9, day=1).isoformat(),
        "date_end": datetime(year=2023, month=9, day=2).isoformat(),
        "reg_deadline": datetime(year=2023, month=8, day=30).isoformat(),
        "max_users": 1000,
        "category_id": CATEGORIES[0].id,
        "address": Address(
            country="Россия",
            city="Санкт-Петербург",
            street="проспект Большевиков",
            house=22,
            corps=1,
            level=1,
        ).dict(),
    },
    {
        "name": "БончВесна",
        "description": "Больше науки богу науки!",
        "date_start": datetime(year=2023, month=5, day=20).isoformat(),
        "date_end": datetime(year=2023, month=6, day=1).isoformat(),
        "reg_deadline": datetime(year=2023, month=5, day=30).isoformat(),
        "max_users": 50,
        "category_id": CATEGORIES[1].id,
        "address": Address(
            country="Россия",
            city="Санкт-Петербург",
            street="проспект Большевиков",
            house=22,
            corps=2,
            level=2,
            office=202,
        ).dict(),
    },
]


EVENTS_READ = [
    {
        "id": 1,
        "name": "Бонч зовёт!",
        "description": "Нам нужен именно ты :)",
        "date_start": datetime(year=2023, month=9, day=1).isoformat(),
        "date_end": datetime(year=2023, month=9, day=2).isoformat(),
        "reg_deadline": datetime(year=2023, month=8, day=30).isoformat(),
        "max_users": 1000,
        "category_id": CATEGORIES[0].id,
        "address": Address(
            country="Россия",
            city="Санкт-Петербург",
            street="проспект Большевиков",
            house=22,
            corps=1,
            level=1,
        ).dict(),
    },
    {
        "id": 2,
        "name": "БончВесна",
        "description": "Больше науки богу науки!",
        "date_start": datetime(year=2023, month=5, day=20).isoformat(),
        "date_end": datetime(year=2023, month=6, day=1).isoformat(),
        "reg_deadline": datetime(year=2023, month=5, day=30).isoformat(),
        "max_users": 50,
        "category_id": CATEGORIES[1].id,
        "address": Address(
            country="Россия",
            city="Санкт-Петербург",
            street="проспект Большевиков",
            house=22,
            corps=2,
            level=2,
            office=202,
        ).dict(),
    },
]

EVENTS_UPDATE = [
    {
        "id": 2,
        "name": "СтудВесна СПбГУТ",
        "description": "Больше науки богу науки!",
        "date_start": datetime(year=2023, month=5, day=20).isoformat(),
        "date_end": datetime(year=2023, month=6, day=1).isoformat(),
        "reg_deadline": datetime(year=2023, month=5, day=30).isoformat(),
        "max_users": 50,
        "category_id": CATEGORIES[1].id,
        "address": Address(
            country="Россия",
            city="Санкт-Петербург",
            street="проспект Большевиков",
            house=22,
            corps=2,
            level=2,
            office=202,
        ).dict(),
    },
]
