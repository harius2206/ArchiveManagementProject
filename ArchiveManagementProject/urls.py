from django.urls import path
from archive_core import views

urlpatterns = [
    # Тепер корінь сайту показує головну сторінку index.html
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('documents/', views.documents_info, name='documents_info'),
]