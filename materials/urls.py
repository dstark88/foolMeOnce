from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    # ex: /materials/
    path('', views.index, name='index'),
]