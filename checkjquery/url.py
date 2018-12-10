from django.urls import path

from .views import jquerycheckView

urlpatterns = [
    path('', jquerycheckView, name='home')
]
