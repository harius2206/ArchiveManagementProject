from .models import Document
from .repositories import DocumentsRepository
from .interfaces import IUnitOfWork

class DjangoUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.documents = DocumentsRepository(Document)

    def save(self):

        pass

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass