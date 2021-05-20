from django.shortcuts import render, redirect 
from django.views.generic.list import ListView
from .models import Task
#from .models import ToDoList

# def index(request):
#     return render(request, 'index.html')

class TaskList(ListView):
    model = Task