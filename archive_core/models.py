from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class Document(models.Model):
    title = models.CharField(
        max_length=70,
        validators=[MinLengthValidator(3)],
        verbose_name="Назва"
    )

    fund_number = models.CharField(
        max_length=100,
        validators=[RegexValidator(r'\A[A-Za-z0-9-]+\z', message="Номер має містити лише латинські літери та цифри")],
        verbose_name="Номер фонду"
    )

    category = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(4)],
        verbose_name="Категорія"
    )

    creation_date = models.DateField(null=True, blank=True, verbose_name="Дата створення")
    archivist_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Архіваріус")
    note = models.TextField(null=True, blank=True, verbose_name="Примітка")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")

    def __str__(self):
        return self.title