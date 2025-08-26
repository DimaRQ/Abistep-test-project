from decimal import Decimal


class InMemoryDB:
    def __init__(self):
        self.users = {}

        self.users[1] = {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "balance": Decimal("100.00"),
        }
        self.users[2] = {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com",
            "balance": Decimal("50.00"),
        }


db = InMemoryDB()
