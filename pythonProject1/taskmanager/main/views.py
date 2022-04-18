from django.shortcuts import render
from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request,'main/index.html', {'title': 'Головна сторінка сайту', 'tasks': tasks})


def abaut(request):
    tasks = Task.objects.all()
    return render(request,'main/Abaut.html', {'title': 'Послуги', 'tasks': tasks})

