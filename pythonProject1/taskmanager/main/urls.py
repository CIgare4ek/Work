from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('abaut', views.abaut, name='abaut')
]