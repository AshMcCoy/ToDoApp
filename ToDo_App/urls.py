from django.urls import path
from .views import (index)

app_name = 'ToDo_App'

urlpatterns = [
    path('', index, name = "index"),
]