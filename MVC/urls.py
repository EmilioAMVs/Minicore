# core/urls.py
from django.urls import path
from .controller import filtrar_gastos

urlpatterns = [
    path('', filtrar_gastos, name='filtrar_gastos'),
]
