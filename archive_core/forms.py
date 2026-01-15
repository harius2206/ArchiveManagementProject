from django import forms
from .models import Document

# Завдання 3.2: Клас для створення списків вибору (аналог SelectListCreation)
CATEGORY_CHOICES = [
    ('', '--- Виберіть категорію ---'),
    ('Адміністративні', 'Адміністративні'),
    ('Кадрові', 'Кадрові'),
    ('Технічні', 'Технічні'),
]

class DocumentEditingForm(forms.ModelForm):
    # Використання списку вибору для категорії
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Категорія")

    class Meta:
        model = Document
        fields = ['title', 'fund_number', 'category', 'creation_date', 'archivist_name', 'note', 'description']
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'note': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }

class DocumentBrowsingModel:
    def __init__(self, doc_obj):
        self.id = doc_obj.id
        self.title = doc_obj.title
        self.fund_number = doc_obj.fund_number
        self.category = doc_obj.category