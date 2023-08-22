from django.urls import path
from . import views

app_name = 'm9'

urlpatterns = [
    path('', views.index, name='index')
]
