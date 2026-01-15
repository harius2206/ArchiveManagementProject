from django.urls import path
from archive_core import views

urlpatterns = [
    # За замовчуванням відкриваємо список документів 
    path('', views.documents_info, name='index'), 
    path('about/', views.about, name='about'),
    path('documents/', views.documents_info, name='documents_info'),
]