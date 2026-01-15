from django.shortcuts import render, redirect
from .uow import DjangoUnitOfWork
from .forms import DocumentEditingForm, DocumentBrowsingModel
from .models import Document

# Завдання 2: Список (Index)
def crud_index(request):
    with DjangoUnitOfWork() as uow:
        # Отримуємо всі об'єкти та приводимо до BrowsingModel
        documents = uow.documents.get_all().order_by('title')
        browsing_model = [DocumentBrowsingModel(d) for d in documents]
        return render(request, 'archivel_core/crud_index.html', {'model': browsing_model})

# Завдання 3: Створення (Create)
def document_create(request):
    uow = DjangoUnitOfWork()
    if request.method == 'POST':
        form = DocumentEditingForm(request.POST)
        if form.is_valid():
            # Завдання 3.10.a: Додання у сховище через репозиторій
            new_doc = form.save(commit=False)
            uow.documents.add(new_doc)
            uow.save()
            return redirect('crud_index')
    else:
        form = DocumentEditingForm()
    return render(request, 'archivel_core/document_form.html', {'form': form, 'title': 'Створення документа'})

# Завдання 4: Редагування (Edit)
def document_edit(request, id):
    uow = DjangoUnitOfWork()
    doc = get_object_or_404(Document, id=id)
    if request.method == 'POST':
        form = DocumentEditingForm(request.POST, instance=doc)
        if form.is_valid():
            updated_doc = form.save(commit=False)
            uow.documents.update(updated_doc) # Виклик методу Update репозиторію
            uow.save()
            return redirect('crud_index')
    else:
        form = DocumentEditingForm(instance=doc)
    return render(request, 'archivel_core/document_form.html', {'form': form, 'title': 'Редагування'})

# Завдання 5: Видалення (Delete)
def document_delete(request, id):
    uow = DjangoUnitOfWork()
    doc = get_object_or_404(Document, id=id)
    if request.method == 'POST':
        uow.documents.delete(id) # Видалення через репозиторій
        uow.save()
        return redirect('crud_index')
    return render(request, 'archivel_core/document_confirm_delete.html', {'object': doc})

# Завдання 6: Деталі (Details)
def document_details(request, id):
    doc = get_object_or_404(Document, id=id)
    return render(request, 'archivel_core/document_details.html', {'object': doc})