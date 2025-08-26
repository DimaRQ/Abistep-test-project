# Структура проекта
```
src/
├── app/
│ ├── v1/
│ │ ├── user/
│ │ │ ├── router.py # роутеры для пользователей
│ │ │ └── schemas.py # схемы для роутеров user
│ │ └── wallet/
│ │ ├── router.py # роутер для переводов
│ │ └── schemas.py # схемы для wallet
│ │
│ └── api.py # подключение всех роутеров в v1
│
├── core/
│ └──config.py # конфигурация (settings)
│
├── db/
│ └── session.py # Хранение данных в памяти
│
├── tests/
│ ├── test_user.py # тесты пользователей
│ └── test_wallet.py # тесты переводов
│
└── main.py # точка входа
```

---

# Документация

- Swagger `http://localhost:8000/docs`
- Redoc `http://localhost:8000/redoc`

---

# Тесты

Тесты написаны на pytest + httpx

Запуск тестов:
```bash
python -m pytest
```

---

# Форматирование

Форматировние через black

```bash
black .
```