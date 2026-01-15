from django.core.management.base import BaseCommand
from archive_core.uow import DjangoUnitOfWork
from archive_core.utils import to_line_list, create_testing_data


class Command(BaseCommand):
    help = 'Перевірка роботи Unit of Work та Repositories'

    def handle(self, *args, **kwargs):
        self.stdout.write(" --- StudyUOW (Django Version) ---")

        with DjangoUnitOfWork() as uow:
            create_testing_data(uow)

            all_docs = uow.documents.get_all()
            self.stdout.write(to_line_list(all_docs, "Список документів в архіві"))

            uow.save()
            self.stdout.write(self.style.SUCCESS("Дані успішно оброблені через UOW"))