from django.urls import path
from .views import ariza

urlpatterns = [
    path('', ariza, name='ariza'),
]