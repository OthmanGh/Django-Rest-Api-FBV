from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.get_notes, name='get_notes')
]
