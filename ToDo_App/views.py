from django.shortcuts import render, redirect 
#from .models import ToDoList

def index(request):
    return render(request, 'index.html')

# Create your views here.
