from django import forms
from .models import Document


class DocumentEditingForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'fund_number', 'category', 'creation_date', 'archivist_name', 'note', 'description']
        widgets = {
            'creation_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': 3}),
            'description': forms.Textarea(attrs={'rows': 5}),
        }


class DocumentBrowsingModel:
    def __init__(self, doc_obj):
        self.id = doc_obj.id
        self.title = doc_obj.title
        self.fund_number = doc_obj.fund_number
        self.category = doc_obj.category