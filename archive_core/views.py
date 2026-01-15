from django.shortcuts import render, redirect, get_object_or_404
from .uow import DjangoUnitOfWork
from .forms import DocumentEditingForm, DocumentBrowsingModel
from .models import Document

# Головна сторінка
def index(request):
    return render(request, 'archive_core/index.html')

# Про сайт
def about(request):
    return render(request, 'archive_core/about.html')

def crud_index(request):
    with DjangoUnitOfWork() as uow:
        documents = uow.documents.get_all().order_by('title')
        browsing_model = [DocumentBrowsingModel(d) for d in documents]
        return render(request, 'archive_core/crud_index.html', {'model': browsing_model})

def document_create(request):
    uow = DjangoUnitOfWork()
    if request.method == 'POST':
        form = DocumentEditingForm(request.POST)
        if form.is_valid():
            new_doc = form.save(commit=False)
            uow.documents.add(new_doc)
            uow.save()
            return redirect('documents_info')
    else:
        form = DocumentEditingForm()
    return render(request, 'archive_core/document_form.html', {'form': form, 'title': 'Створення документа'})

def document_edit(request, id):
    uow = DjangoUnitOfWork()
    doc = get_object_or_404(Document, id=id)
    if request.method == 'POST':
        form = DocumentEditingForm(request.POST, instance=doc)
        if form.is_valid():
            updated_doc = form.save(commit=False)
            uow.documents.update(updated_doc)
            uow.save()
            return redirect('documents_info')
    else:
        form = DocumentEditingForm(instance=doc)
    return render(request, 'archive_core/document_form.html', {'form': form, 'title': 'Редагування'})

def document_delete(request, id):
    uow = DjangoUnitOfWork()
    doc = get_object_or_404(Document, id=id)
    if request.method == 'POST':
        uow.documents.delete(id)
        uow.save()
        return redirect('documents_info')
    return render(request, 'archive_core/document_confirm_delete.html', {'object': doc})

def document_details(request, id):
    doc = get_object_or_404(Document, id=id)
    return render(request, 'archive_core/document_details.html', {'object': doc})