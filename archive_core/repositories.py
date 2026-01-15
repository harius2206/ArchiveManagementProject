from .interfaces import IDocumentsRepository

class DocumentsRepository(IDocumentsRepository):
    def __init__(self, model):
        self._model = model

    def get_all(self):
        return self._model.objects.all()

    def get_by_id(self, id):
        return self._model.objects.filter(id=id).first()

    def add(self, item):
        item.save()

    def update(self, item):
        existing = self.get_by_id(item.id)
        if existing:
            existing.title = item.title
            existing.fund_number = item.fund_number
            existing.category = item.category
            existing.creation_date = item.creation_date
            existing.archivist_name = item.archivist_name
            existing.save()

    def delete(self, id):
        item = self.get_by_id(id)
        if item:
            item.delete()