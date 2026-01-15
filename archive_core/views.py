from django.shortcuts import render
from .uow import DjangoUnitOfWork

# Аналог HomeController.Index [cite: 3, 6]
def index(request):
    return render(request, 'archivel_core/index.html')

# Аналог HomeController.About
def about(request):
    return render(request, 'archivel_core/about.html')

# Аналог DocumentsController.ObjectsInfo
def documents_info(request):
    uow = DjangoUnitOfWork()
    objects = uow.documents.get_all() # Отримуємо дані через репозиторій
    return render(request, 'archivel_core/_objects_info.html', {'model': objects})