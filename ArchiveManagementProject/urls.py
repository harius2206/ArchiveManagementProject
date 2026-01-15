from django.urls import path
from archive_core import views

urlpatterns = [
    path('', views.crud_index, name='crud_index'), # Default route
    path('create/', views.document_create, name='document_create'),
    path('edit/<int:id>/', views.document_edit, name='document_edit'),
    path('delete/<int:id>/', views.document_delete, name='document_delete'),
    path('details/<int:id>/', views.document_details, name='document_details'),
    path('about/', views.about, name='about'),
]