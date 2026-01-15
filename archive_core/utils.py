from datetime import date
from .models import Document

def to_line_list(collection, prompt):
    items = "\n".join([str(item) for item in collection])
    return f"{prompt}:\n{items}\n"

def create_testing_data(uow):
    # Створюємо тестові документи, якщо база порожня
    if not uow.documents.get_all().exists():
        docs = [
            Document(title="Акт передачі", fund_number="Ф-123", category="Адміністративні", creation_date=date(2023, 10, 15)),
            Document(title="Наказ про призначення", fund_number="Ф-456", category="Кадрові", creation_date=date(2024, 1, 20)),
            Document(title="Листування", fund_number="Ф-789", category="Офіційні листи")
        ]
        for d in docs:
            uow.documents.add(d)