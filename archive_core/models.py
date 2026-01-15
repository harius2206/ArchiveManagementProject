from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="Назва")
    fund_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Номер фонду")
    category = models.CharField(max_length=150, null=True, blank=True, verbose_name="Категорія")
    creation_date = models.DateField(null=True, blank=True, verbose_name="Дата створення")
    archivist_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Архіваріус")
    note = models.TextField(null=True, blank=True, verbose_name="Примітка")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")

    def __str__(self):
        date_str = self.creation_date.strftime('%d.%m.%Y') if self.creation_date else "Невказано"
        return f"Документ №{self.id}: {self.title or 'Невказано'} (Фонд: {self.fund_number or 'Невказано'})"